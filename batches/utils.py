from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import os
import base64
import io
from PIL import Image
# import re



#pagination super class
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


#factory method for form creation
def createForm(request, template, classFrom):
    form = classFrom()
    context = {'form' : form}
    return render(request, template, context)


#factory method for card search
def createSearch(request, form, params, model_class, template):
    if request.method == 'GET':
        form = form()
        if form.is_valid():
            query = Q()
            for param, field in params.items():
                value = form.cleaned_data.get(param, '')
                if value:
                    query &= Q(**{field:value})

                results = model_class.objects.filter(query) if query else model_class.objects.none()
                result_count = results.count() if query else 0
                custom_range, results = paginate(request, results)
                context = {'form':form, 'results': results,
                            'result_count':result_count, 'custom_range':custom_range}
                return render(request, template, context)
    context = {'from': form, 'results':model_class.objects.none(), result_count:0}
    return redirect(template)


#display images
def singleImageView(request, pk, doc_model, obj_model, card_form):

    # form = None
    ids = request.GET.get('ids', '')
    ids_list = ids.split(',') if ids else []

    previous_page_url = request.session.get('first_previous_page_url', None)
    print('previous url', previous_page_url)
    if previous_page_url is None:
        previous_page_url = request.META.get('HTTP_REFERER', None)
        request.session['first_previous_page_url'] = previous_page_url


    image_data = view_image(pk, obj_model)
    print('image data --------->', len(image_data))
    print('----------------')
    form = edit_document(request, pk, doc_model, card_form)
    first_doc, last_doc, next_doc, prev_doc = navigate_image(ids_list, pk)
    deleted = delete_document(request, pk, ids_list, doc_model, obj_model)
    print('---------pk',pk)
    print('---------next doc',next_doc)
    print('------prev doc',prev_doc)
    print('--------first doc',first_doc)
    print('------last doc',last_doc)
    print('------list',ids_list)

 
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
        'ids_list':ids_list,
        'pk': pk,
        'form': form,
        'first_doc': first_doc,
        'last_doc': last_doc,
        'next_doc': next_doc,
        'prev_doc': prev_doc,
        'previous_page_url': previous_page_url,
        }

    return render(request, 'batches/single-image.html', context)

#navigate images
def navigate_image(ids_list, current_id):
    try:
        index = ids_list.index(current_id)
    except ValueError:
        return None, None, None, None

    
    first_id = ids_list[0] if ids_list else None
    last_id = ids_list[-1] if ids_list else None
    
    if index == 0:
        prev_id = None
    else:
        prev_id = ids_list[index - 1]

    if index == len(ids_list) - 1:
        next_id = None
    else:
        next_id = ids_list[index + 1]
    
    return first_id, last_id, next_id, prev_id



#view image
def view_image(pk, obj_model):
    # image = PvdmObjs116.objects.filter(docid=pk).first()
    images = obj_model.objects.filter(docid=pk)
    # image_data = None
    images_data = []
    print("Number of images found:", len(images))

    for image in images:
    # if image:
        dg_id = image.dgid
        dg_query = PvdmDg1.objects.filter(dgid=dg_id).first()
        if dg_query:
            filelist = image.filelist
            filenames = extract_filenames_base(filelist)
            for filename in filenames:
                path = os.path.join(dg_query.path, filename)
                try:
                    with Image.open(path) as img:
                        output = io.BytesIO()
                        img.convert("RGB").save(output, format="JPEG")
                        image_data = base64.b64encode(output.getvalue()).decode('utf-8')
                        images_data.append(image_data)
                except FileNotFoundError:
                # image_data = None
                    pass

    print('filenames ------>',filenames)
    print("Number of images processed:", len(images_data))
    
    # print("image data ---->:", images_data)
    return images_data


def extract_filenames_base(filelist):
    if "Images" in filelist:
        return extract_filenames_extension_pattern(filelist)
    elif all(char.isalpha() for char in filelist):
        return extract_filenames_byts_pattern(filelist)
    else:
        return extract_filenames(filelist)





#make a list of images if filelist has more than 1
def extract_filenames(filelist):
    filenames = []
    current_filename = ''
    for char in filelist:
        if char.isdigit():
            current_filename += char

        elif char == '.':
            filenames.append(current_filename + '.JPG')
            current_filename = ''

    if current_filename:
        filenames.append(current_filename + ".JPG")
            
    return filenames



def extract_filenames_extension_pattern(filelist):
    filenames = []
    current_filename = ''
    for char in filelist:
        current_filename += char
        if current_filename.endswith('Images'):
            image_filename = current_filename[:-len('Images')]
            filenames.append(image_filename)
            current_filename = 'Images'
    
    if current_filename:
        filenames.append(current_filename)
    
    return filenames


def extract_filenames_byts_pattern(filelist, filename_length=8):
    filenames = []
    num_filenames = len(filelist)
    for i in range(num_filenames):
        start_idx = i * filename_length
        end_idx = start_idx + filename_length
        filenames.append(filelist[start_idx:end_idx])

    return filenames

#edit document
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
        form = UpdateBondBooks(instance=data)

    return form

#delete document
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


#handle ajax request
# def ajax_func(request):
#     if request.method == 'GET' and request.is_ajax():
#         item_id = request.GET.get('item_id')
#         return item_id

#update form data
# def update_form_data(request, pk):
    
#     return edit_document(request, pk)





    
