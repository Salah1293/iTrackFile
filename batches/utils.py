import logging
from pipes import quote
from django.shortcuts import render, redirect

from iTrackFiles import settings
from .models import *
from django.db.models import Q, Value
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os
import base64
import io
from PIL import Image
import re
from django.utils.dateformat import DateFormat


# pagination super class
def paginate(request, query):
    page = request.GET.get('page')
    result = 50
    paginator = Paginator(query, result)

    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        query = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        query = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, query


# factory method for form creation for intial search THAT SERVERSES ALL SECTIONS
def createForm(request, template, classFrom):
    form = classFrom()
    context = {'form': form}
    return render(request, template, context)



# display images contains evrey thing in page except print Rotat and reset mmade by js as they are styling manner
def singleImageView(request, pk, doc_model, obj_model, card_form, section):
    # contains id for all rows displayed
    ids = request.GET.get('ids', '')
    ids_list = ids.split(',') if ids else []

    previous_page_url = request.session.get('first_previous_page_url', None)
    if previous_page_url is None:
        previous_page_url = request.META.get('HTTP_REFERER', None)
        request.session['first_previous_page_url'] = previous_page_url

    image_data = view_image(pk, obj_model)

    form = edit_document(request, pk, doc_model, card_form)
    first_doc, last_doc, next_doc, prev_doc = navigate_image(ids_list, pk)
    deleted = delete_document(request, pk, ids_list, doc_model, obj_model)

    if deleted:
        if next_doc:
            pk = next_doc
        elif prev_doc:
            pk = prev_doc
        else:
            pk = None

        image_data = view_image(pk, obj_model)
        first_doc, last_doc, next_doc, prev_doc = navigate_image(ids_list, pk)
        form = edit_document(request, pk, doc_model, card_form)

    context = {
        'image_data': image_data,
        'image_data_length': len(image_data),
        'ids_list': ids_list,
        'pk': pk,
        'form': form,
        'first_doc': first_doc,
        'last_doc': last_doc,
        'next_doc': next_doc,
        'prev_doc': prev_doc,
        'previous_page_url': previous_page_url,
        'section': section
    }

    return render(request, 'batches/single-image.html', context)


# view image FOR THE PREVIOUS FUNCTION
def view_image(pk, obj_model):
    images = obj_model.objects.filter(docid=pk)
    images_data = []

    for image in images:
        dg_id = image.dgid
        dg_query = PvdmDg1.objects.filter(dgid=dg_id).first()
        if dg_query:
            filelist = image.filelist
            filenames = extract_filenames_base(filelist)

            for filename in filenames:
                if filename.isdigit() and len(filename) == 8:
                    path = os.path.join(
                        dg_query.path + dg_query.origdgname + '/IMG1/00000/', filename + '.TIF')
                else:
                    path = os.path.join(dg_query.path, filename)
                try:
                    with Image.open(path) as img:
                        output = io.BytesIO()
                        img.convert("RGB").save(output, format="JPEG")
                        image_data = base64.b64encode(
                            output.getvalue()).decode('utf-8')
                        images_data.append(image_data)
                except FileNotFoundError:
                    pass

    return images_data


# navigate images FOR ICONS LAST PREVIOUS AND NEXT
def navigate_image(ids_list, current_id):
    try:
        current_index = ids_list.index(current_id)
    except ValueError:
        return None, None, None, None

    first_id = ids_list[0] if ids_list else None
    last_id = ids_list[-1] if ids_list else None

    if current_index == 0:
        prev_id = None
    else:
        prev_id = ids_list[current_index - 1]

    if current_index == len(ids_list) - 1:
        next_id = None
    else:
        next_id = ids_list[current_index + 1]
    return first_id, last_id, next_id, prev_id


# BASE FUNCTION THAT HAS CONDITIONS FOR EACH IMAGE PATTERN PATHES FUNCTIONS
def extract_filenames_base(filelist):
    if len(filelist) % 8 == 0 and all(char.isdigit() for char in filelist):
        return extract_filenames_byts_pattern(filelist)
    
    elif '<PATH>' in filelist:
        return extract_filenames_path_pattern(filelist)
    
    elif "Images" in filelist:
        return extract_filenames_extension_pattern(filelist)

    else:
        raise ValueError("Filelist does not match any known pattern")

# SERVE PATTERN FOR 0000001
def extract_filenames_byts_pattern(filelist):
    filenames = [filelist[i:i+8] for i in range(0, len(filelist), 8)]
    return filenames

# SERVE PATTERN IMAGES/0/0/0/0001.TIF
def extract_filenames_extension_pattern(filelist):
    filenames = []
    current_filename = ''
    pattern_prefix = 'Images'

    for char in filelist:
        current_filename += char

        if current_filename.endswith(pattern_prefix):
            image_filename = current_filename[:-len(pattern_prefix)].strip()
            if image_filename:
                filenames.append(image_filename)
            current_filename = pattern_prefix

    if current_filename and current_filename != pattern_prefix:
        filenames.append(current_filename.strip())

    return filenames

#SERVE PATH PATEREN
def extract_filenames_path_pattern(filelist):
    pattern = re.compile(r'<PATH>(.*?)</PATH>')
    return pattern.findall(filelist)

# EDIT FUNCTIONS
def edit_document(request, pk, doc_model, card_form):
    form = None
    if request.method == 'POST':
        if 'edit' in request.POST:
            data = doc_model.objects.get(docid=pk)
            form = card_form(request.POST, instance=data)
            if form.is_valid():
                form.save()
        else:
            data = doc_model.objects.get(docid=pk)
            form = card_form(instance=data)
    else:
        data = doc_model.objects.get(docid=pk)
        form = card_form(instance=data)
    return form

# delete document
def delete_document(request, pk, ids_list, doc_model, obj_model):
    if request.method == 'POST':
        if 'delete' in request.POST:
            document = obj_model.objects.filter(docid=pk).first()
            if document:
                document_metaData = doc_model.objects.filter(docid=pk).first()
                if document_metaData:
                    document_metaData.delete()
                document.delete()
                if pk in ids_list:
                    ids_list.remove(pk)
                return True
    return False

# SERVE GENERAL SERACH
def generate_all_results(query, chosen_section=None):

    criminal = None
    indictments = None
    concealedWeapons = None
    historicOrderBooks = None
    historicIndexCards = None
    destructionOrders = None
    bondBooks = None
    civil = None
    criminalJuvenile = None
    adoption = None
    lawChancery = None
    criminalCases = None
    clerkOrders = None
    charters = None

    criminal_query = (Q(docindex1=query) | Q(docindex3=query) |
                      Q(docindex6=query) | Q(docindex7=query) |
                      Q(docindex10=query))

    indictments_query = (Q(docindex1=query) | Q(docindex2=query) |
                         Q(docindex3=query) | Q(docindex4=query) |
                         Q(docindex5=query) | Q(docindex6=query) |
                         Q(docindex7=query))

    concealed_weapons_query = (Q(docindex1=query) | Q(docindex3=query) |
                               Q(docindex4=query) | Q(docindex7=query) |
                               Q(docindex8=query) | Q(docindex9=query) |
                               Q(docindex10=query))

    historic_order_books_query = (Q(docindex1=query) | Q(docindex2=query) |
                                  Q(docindex3=query))

    historic_index_cards_query = (Q(docindex1=query) | Q(docindex2=query) |
                                  Q(docindex3=query) | Q(docindex5=query) |
                                  Q(docindex6=query) | Q(docindex8=query))

    destruction_orders_query = (Q(docindex1=query))

    bond_books_query = (Q(docindex1=query) | Q(docindex2=query))

    civil_query = (Q(docindex1=query) | Q(docindex3=query) |
                   Q(docindex6=query) | Q(docindex7=query) |
                   Q(docindex8=query) | Q(docindex11=query) |
                   Q(docindex12=query))

    criminal_juvenile_query = (Q(docindex1=query) | Q(docindex3=query) |
                               Q(docindex6=query) | Q(docindex7=query) |
                               Q(docindex11=query) | Q(docindex12=query))

    adoption_query = (Q(docindex1=query) | Q(docindex3=query) |
                      Q(docindex6=query) | Q(docindex7=query) |
                      Q(docindex8=query))

    law_chancery_query = (Q(docindex1=query) | Q(docindex2=query))

    criminal_cases_query = (Q(docindex1=query) | Q(docindex2=query) |
                            Q(docindex3=query) | Q(docindex4=query))

    clerk_orders_query = (Q(docindex1=query) | Q(docindex3=query) |
                          Q(docindex4=query) | Q(docindex6=query) |
                          Q(docindex7=query))

    charters_query = (Q(docindex1=query) | Q(docindex2=query))

    all_results = {}

    if chosen_section:
        if chosen_section == 'Criminal':
            criminal = PvdmDocs11.objects.filter(criminal_query)
            for card in criminal:
                if card.docindex2 or card.docindex20:
                    card.docindex2 = DateFormat(card.docindex2).format('Y-m-d') if card.docindex2 else None
                    card.docindex20 = DateFormat(card.docindex20).format('Y-m-d') if card.docindex20 else None

        elif chosen_section == 'Indictments':
            indictments = PvdmDocs110.objects.filter(indictments_query)
            for card in indictments:
                if card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None
                    card.docindex8 = DateFormat(card.docindex8).format('Y-m-d') if card.docindex8 else None
                    card.docindex9 = DateFormat(card.docindex9).format('Y-m-d') if card.docindex9 else None

        elif chosen_section == 'Concealed Weapons':
            concealedWeapons = PvdmDocs112.objects.filter(
                concealed_weapons_query)
            for card in concealedWeapons:
                if card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None
                    card.docindex2 = DateFormat(card.docindex2).format('Y-m-d') if card.docindex2 else None
                    card.docindex6 = DateFormat(card.docindex6).format('Y-m-d') if card.docindex6 else None
            
        elif chosen_section == 'Historic Order Books':
            historicOrderBooks = PvdmDocs113.objects.filter(
                historic_order_books_query)
            
        elif chosen_section == 'Historic Index Cards':
            historicIndexCards = PvdmDocs114.objects.filter(
                historic_index_cards_query)
            
        elif chosen_section == 'Destruction Orders':
            destructionOrders = PvdmDocs115.objects.filter(
                destruction_orders_query)
            for card in destructionOrders:
                if card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None
                    card.docindex2 = DateFormat(card.docindex2).format('Y-m-d') if card.docindex2 else None
                    card.docindex3 = DateFormat(card.docindex3).format('Y-m-d') if card.docindex3 else None
                    card.docindex4 = DateFormat(card.docindex4).format('Y-m-d') if card.docindex4 else None
                    card.docindex5 = DateFormat(card.docindex5).format('Y-m-d') if card.docindex5 else None
            
        elif chosen_section == 'Bond Books':
            bondBooks = PvdmDocs116.objects.filter(bond_books_query)
            for card in bondBooks:
                if card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None

        elif chosen_section == 'Civil':
            civil = PvdmDocs12.objects.filter(civil_query)
            for card in civil:
                if card.docindex2 or card.docindex20:
                    card.docindex2 = DateFormat(card.docindex2).format('Y-m-d') if card.docindex2 else None
                    card.docindex20 = DateFormat(card.docindex20).format('Y-m-d') if card.docindex20 else None

        elif chosen_section == 'Criminal Juvenile':
            criminalJuvenile = PvdmDocs13.objects.filter(
                criminal_juvenile_query)
            for card in criminalJuvenile:
                if card.docindex2 or card.docindex20:
                    card.docindex2 = DateFormat(card.docindex2).format('Y-m-d') if card.docindex2 else None
                    card.docindex20 = DateFormat(card.docindex20).format('Y-m-d') if card.docindex20 else None

        elif chosen_section == 'Adoption':
            adoption = PvdmDocs14.objects.filter(adoption_query)
            for card in adoption:
                if  card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None
                    card.docindex2 = DateFormat(card.docindex2).format('Y-m-d') if card.docindex2 else None
                    card.docindex20 = DateFormat(card.docindex20).format('Y-m-d') if card.docindex20 else None

        elif chosen_section == 'Law Chancery':
            lawChancery = PvdmDocs16.objects.filter(law_chancery_query)
            for card in lawChancery:
                if card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None

        elif chosen_section == 'Criminal Cases':
            criminalCases = PvdmDocs17.objects.filter(criminal_cases_query)
            for card in criminalCases:
                if card.docindex2 :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None

        elif chosen_section == 'Clerk Orders':
            clerkOrders = PvdmDocs18.objects.filter(clerk_orders_query)
            for card in clerkOrders:
                if  card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None
                    card.docindex2 = DateFormat(card.docindex2).format('Y-m-d') if card.docindex2 else None
                    card.docindex23 = DateFormat(card.docindex23).format('Y-m-d') if card.docindex23 else None

        elif chosen_section == 'Charters':
            charters = PvdmDocs19.objects.filter(charters_query)
            for card in charters:
                if card.createdate :
                    card.createdate = DateFormat(card.createdate).format('Y-m-d') if card.createdate else None

    else:
        criminal = PvdmDocs11.objects.filter(criminal_query)
        indictments = PvdmDocs110.objects.filter(indictments_query)
        concealedWeapons = PvdmDocs112.objects.filter(concealed_weapons_query)
        historicOrderBooks = PvdmDocs113.objects.filter(
            historic_order_books_query)
        historicIndexCards = PvdmDocs114.objects.filter(
            historic_index_cards_query)
        destructionOrders = PvdmDocs115.objects.filter(
            destruction_orders_query)
        bondBooks = PvdmDocs116.objects.filter(bond_books_query)
        civil = PvdmDocs12.objects.filter(civil_query)
        criminalJuvenile = PvdmDocs13.objects.filter(criminal_juvenile_query)
        adoption = PvdmDocs14.objects.filter(adoption_query)
        lawChancery = PvdmDocs16.objects.filter(law_chancery_query)
        criminalCases = PvdmDocs17.objects.filter(criminal_cases_query)
        clerkOrders = PvdmDocs18.objects.filter(clerk_orders_query)
        charters = PvdmDocs19.objects.filter(charters_query)

    all_results = {
        'Criminal': criminal,
        'Indictments': indictments,
        'Concealed Weapons': concealedWeapons,
        'Historic Order Books': historicOrderBooks,
        'Historic Index Cards': historicIndexCards,
        'Destruction Orders': destructionOrders,
        'Bond Books': bondBooks,
        'Civil': civil,
        'Criminal Juvenile': criminalJuvenile,
        'Adoption': adoption,
        'Law Chancery': lawChancery,
        'Criminal Cases': criminalCases,
        'Clerk Orders': clerkOrders,
        'Charters': charters
    }

    all_results = {key: value for key, value in all_results.items() if value}

    

    return all_results

# GET TABLE NAME THAT HAS THE KEYWORD THAT THE USER USED FOR SERRCH
def get_section_name(chosen_section):

    model_mapping = {
        'Criminal': 'criminal',
        'Indictments': 'indictments',
        'Concealed Weapons': 'concealed-weapons',
        'Historic Order Books': 'historic-order-books',
        'Historic Index Cards': 'historic-index-cards',
        'Destruction Orders': 'destruction-orders',
        'Bond Books': 'bond',
        'Civil': 'civil',
        'Criminal Juvenile': 'criminal-juvenile',
        'Adoption': 'adoption',
        'Law Chancery': 'law-chancery',
        'Criminal Cases': 'criminal-cases',
        'Clerk Orders': 'clerk-orders',
        'Charters': 'charters'
    }

    return model_mapping.get(chosen_section, None)
