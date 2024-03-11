from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .utils import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.http import FileResponse, HttpResponse
import os
import base64
import io
from PIL import Image

# Create your views here.


def deleteBatch (request):

    return render(request , 'batches/delete-batch.html')

def updateBatch (request):

    return render(request , 'batches/update-batch.html')

def incompleteBatch (request):
    civil = PvdmDocs12.objects.all()
    context = {'civil':civil}

    return render(request , 'batches/incomplete-batches.html', context)

def fillingBatch (request):

    return render(request , 'batches/filling-batch.html')

def landingBatches (request):

    return render(request , 'batches/landing-page.html')

# def singleBatch (request):

#     return render(request , 'batches/single-batch.html')

def newBatch (request):

    return render(request , 'batches/new-batch.html')

def scannerSetting (request):

    return render(request , 'batches/scanner-setting.html')

def capture (request):

    return render(request , 'batches/capture.html')

#criminal search
def criminalSearch(request):
    return createForm(request, 'batches/criminal-search.html', CriminalForm)

#criminal display resylts
def criminalResults (request):

    form = CriminalForm()
    
    if request.method == "GET":
        form = CriminalForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            defendant_last_name = form.cleaned_data.get('docindex6', '')
            defendant_first_name = form.cleaned_data.get('docindex7', '')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if start_date and end_date:
                query &= Q(docindex2__range=[start_date, end_date])
            if defendant_last_name:
                query &= Q(docindex6=defendant_last_name)
            if defendant_first_name:
                query &= Q(docindex7=defendant_first_name)
                
            criminal = PvdmDocs11.objects.filter(query) if query else PvdmDocs11.objects.none()

            resultCount = criminal.count() if query else 0

            custom_range, criminal = paginate(request, criminal)
                    
            context = {'form': form, 'criminal': criminal,
                       'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/criminal-results.html', context)

    context={'form' : form, 'criminal' : PvdmDocs11.objects.none(), 'resultCount' : 0}    
    return redirect('criminalResults')


#civil search
def civilSearch (request):
    return createForm(request, 'batches/civil-search.html', CivilForm)


#civil display resylts
def civilResults (request):
    form = CivilForm()

    if request.method == 'GET':
        form = CivilForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('case_number', '')
            last_name = form.cleaned_data.get('last_name', '')
            first_name = form.cleaned_data.get('first_name', '')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')

           
            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if start_date and end_date:
                query &= Q(docindex2__range=[start_date, end_date])

            if last_name:
                query &= (Q(docindex11=last_name) | Q(docindex6=last_name) |
                          Q(docindex16=last_name))
                
            if first_name:
                query &= (Q(docindex12=first_name) | Q(docindex7=first_name) |
                          Q(docindex17=first_name))
                
            # if last_name and not (case_number or start_date or end_date or first_name):
            #     query &= (Q(docindex11=last_name) | Q(docindex6=last_name))

            # if first_name and not (case_number or start_date or end_date or last_name):
            #     query &= (Q(docindex12=first_name) | Q(docindex7=first_name))
            


            civil = PvdmDocs12.objects.filter(query) if query else PvdmDocs12.objects.none()

            resultCount = civil.count() if query else 0

            custom_range, civil = paginate(request, civil)

            #     civil = PvdmDocs12.objects.none()

            context = {'form': form, 'civil': civil,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/civil-results.html', context)
        
    
    context={'form' : form, 'civil' : PvdmDocs12.objects.none(), 'resultCount' : 0}    
    return redirect('civilResults')


#criminal cases search
def criminalCasesSearch (request):
    return createForm(request, 'batches/criminal-cases-search.html', CriminalCasesForm)


#criminal cases display results
def criminalCasesResults(request):
    form = CriminalCasesForm()
    if request.method == "GET":
        form = CriminalCasesForm(request.GET)
        if form.is_valid():
            date = form.cleaned_data.get('docindex1', '')
            case_number = form.cleaned_data.get('docindex2', '')
            last_Corporation = form.cleaned_data.get('docindex3', '')
            first = form.cleaned_data.get('docindex4', '')

            
            query = Q()

            
            if date:
                query &= Q(docindex1=date)
            if case_number:
                query &= Q(docindex2=case_number)
            if last_Corporation:
                query &= Q(docindex3=last_Corporation)
            if first:
                query &= Q(docindex4=first)


            criminalCases = PvdmDocs17.objects.filter(query) if query else PvdmDocs17.objects.none()

            resultCount = criminalCases.count() if query else 0

            custom_range, criminalCases = paginate(request, criminalCases)

            context = {'form': form, 'criminalCases': criminalCases,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/criminal-cases-results.html', context)
        
    
    context={'form' : form, 'criminalCases' : PvdmDocs17.objects.none(), 'resultCount' : 0}    
    return redirect('criminalCasesResults')
        

#criminal junevile search
def criminalJuvenileSearch (request):
    return createForm(request, 'batches/criminal-juvenile-Search.html', CriminalJuvenileForm)


#criminal junevile display results
def criminalJuvenileResults (request):
    form = CriminalJuvenileForm()
    if request.method == 'GET':
        form = CriminalJuvenileForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            defendant_last_name = form.cleaned_data.get('docindex6', '')
            defendant_first_name = form.cleaned_data.get('docindex7', '')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')


            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if start_date and end_date:
                query &= Q(docindex2__range=[start_date, end_date])
            if defendant_last_name:
                query &= Q(docindex6=defendant_last_name)
            if defendant_first_name:
                query &= Q(docindex7=defendant_first_name)


            ciminalJuvenile = PvdmDocs13.objects.filter(query) if query else PvdmDocs13.objects.none()

            resultCount = ciminalJuvenile.count() if query else 0

            custom_range, ciminalJuvenile = paginate(request, ciminalJuvenile)

            context = {'form' : form,'ciminalJuvenile' : ciminalJuvenile,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/criminal-juvenile-results.html', context)
        
    
    context={'form' : form, 'ciminalJuvenile' : PvdmDocs13.objects.none(), 'resultCount' : 0}    
    return redirect('criminalJuvenileResults')

   
#historic index cards search
def historicIndexCardsSearch (request):
    return createForm(request, 'batches/hisoric-index-cards-search.html', HistoricIndexCardsForm)


#historic index cards display results
def historicIndexCardsResults(request):
    form = HistoricIndexCardsForm()
    if request.method == 'GET':
        form = HistoricIndexCardsForm(request.GET)
        if form.is_valid():
            last_name = form.cleaned_data.get('docindex1', '')
            first_name = form.cleaned_data.get('docindex2', '')


            query = Q()

            if last_name:
                query &= Q(docindex1=last_name)
            if first_name:
                query &= Q(docindex2=first_name)


            historicIndexCards = PvdmDocs114.objects.filter(query) if query else PvdmDocs114.objects.none()

            resultCount = historicIndexCards.count() if query else 0

            custom_range, historicIndexCards = paginate(request, historicIndexCards)

            context = {'form' : form, 'historicIndexCards': historicIndexCards, 
                       'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/historic-index-cards-results.html', context)
        

    context = {'form' : form, 'historicIndexCards' : PvdmDocs114.objects.none(), 'resultCount' : 0}
    return redirect('hitoricIndexCardsResults')


#historic order books search
def historicOrderBooksSearch (request):
    return createForm(request, 'batches/historic-order-books-Search.html', HistoricOrderBooksForm)


#historic order books display results
def historicOrderBooksResults(request):
    form = HistoricOrderBooksForm()
    
    if request.method == 'GET':
        form = HistoricOrderBooksForm(request.GET)
        if form.is_valid():
            year = form.cleaned_data.get('docindex2', '')


            query = Q()

            if year:
                query &= Q(docindex1=year)


            historicOrderBooks = PvdmDocs113.objects.filter(query) if query else PvdmDocs113.objects.none()

            resultCount = historicOrderBooks.count() if query else 0

            custom_range, historicOrderBooks = paginate(request, historicOrderBooks)

            context = {'form' : form, 'historicOrderBooks' : historicOrderBooks,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/historic-order-books-results.html', context)

    context = {'form' : form, 'historicOrderBooks' : PvdmDocs113.objects.none(), 'resultCount' : 0}
    return redirect('historicOrderBooks')


#he search
def hrSearch (request):
    return createForm(request, 'batches/hr-search.html', HrForm)

#hr display results
def hrResults(request):

    form = HrForm()
    if request.method == 'GET':
        form = HrForm(request.GET)
        if form.is_valid():
            last_name = form.cleaned_data.get('docindex1', '')
            first_name = form.cleaned_data.get('docindex2', '')
            ein = form.cleaned_data.get('docindex3', '')


            query = Q()

            if last_name:
                query &= Q(docindex1=last_name)
            if first_name:
                query &= Q(docindex2=first_name)
            if ein:
                query &= Q(docindex3=ein)


            hr = PvdmDocs15.objects.filter(query) if query else PvdmDocs15.objects.none()

            resultCount = hr.count() if query else 0

            custom_range, hr = paginate(request, hr)

            context = {'form' : form, 'hr' : hr,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/hr-results.html', context)
        

    context = {'form' : form, 'hr' : PvdmDocs15.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/hr-results.html', context)


#bond books search
def bondBooksSearch(request):
    return createForm(request, 'batches/bond-books-search.html', BondBooksForm)

#bond books display results
def bondBooksResults(request):
    form = BondBooksForm()
    if request.method == 'GET':
        form = BondBooksForm(request.GET)
        if form.is_valid():
            book = form.cleaned_data.get('docindex1', '')
            page = form.cleaned_data.get('docindex2', '')
            

            query = Q()

            if book:
                query &= Q(docindex1=book)
            if page:
                query &= Q(docindex2=page)
            

            bondBooks = PvdmDocs116.objects.filter(query) if query else PvdmDocs116.objects.none()

            resultCount = bondBooks.count() if query else 0

            custom_range, bondBooks = paginate(request, bondBooks)

            context = {'form' : form, 'bondBooks' : bondBooks,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/bond-books-results.html', context)
        

    context = {'form' : form, 'bondBooks' : PvdmDocs116.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/bond-books-results.html', context)
    

#charters search
def chartersSearch(request):
    return createForm(request, 'batches/charters-search.html', ChartersForm)


#charters display results
def chartersResults(request):
    form = ChartersForm()
    if request.method == 'GET':
        form = ChartersForm(request.GET)
        if form.is_valid():
            charter_name = form.cleaned_data.get('docindex1', '')
            book = form.cleaned_data.get('docindex2', '')
            page = form.cleaned_data.get('docindex3', '')


            query = Q()

            if charter_name:
                query &= Q(docindex1=charter_name)
            if book:
                query &= Q(docindex2=book)
            if page:
                query &= Q(docindex3=page)


            charters = PvdmDocs19.objects.filter(query) if query else PvdmDocs19.objects.none()

            resultCount = charters.count() if query else 0

            custom_range, charters = paginate(request, charters)

            context = {'form' : form, 'charters' : charters,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/charters-results.html', context)
        

    context = {'form' : form, 'charters' : PvdmDocs19.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/charters-results.html', context)


#concealed weapons search
def ConcealedWeaponsSearch(request):
    return createForm(request, 'batches/concealed-weapons-search.html', ConcealedWeaponsForm)


#concealed weapons display results
def ConcealedWeaponsResults(request):

    form = ConcealedWeaponsForm()
    if request.method == 'GET':
        form = ConcealedWeaponsForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            subject_company = form.cleaned_data.get('docindex7', '')
            subject_last_name = form.cleaned_data.get('docindex8', '')
            subject_first_name = form.cleaned_data.get('docindex9', '')


            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if subject_company:
                query &= Q(docindex7=subject_company)
            if subject_last_name:
                query &= Q(docindex8=subject_last_name)
            if subject_first_name:
                query &= Q(docindex9=subject_first_name)


            concealedWeapons = PvdmDocs112.objects.filter(query) if query else PvdmDocs112.objects.none()

            resultCount = concealedWeapons.count() if query else 0

            custom_range, concealedWeapons = paginate(request, concealedWeapons)

            context = {'form' : form, 'concealedWeapons' : concealedWeapons,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/concealed-weapons-results.html', context)
        

    context = {'form' : form, 'concealedWeapons' : PvdmDocs112.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/concealed-weapons-results.html', context)


#indictmenys search
def indictmentsSearch(request):
    return createForm(request, 'batches/indictments-search.html', IndictmentsForm)


#indictmenys display results
def indictmentsResults(request):
    form = IndictmentsForm()
    if request.method == 'GET':
        form = IndictmentsForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            defendant_first_name = form.cleaned_data.get('docindex3', '')
            defendant_last_name = form.cleaned_data.get('docindex5', '')


            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if defendant_first_name:
                query &= Q(docindex3=defendant_first_name)
            if defendant_last_name:
                query &= Q(docindex5=defendant_last_name)


            indictments = PvdmDocs110.objects.filter(query) if query else PvdmDocs110.objects.none()

            resultCount = indictments.count() if query else 0

            custom_range, indictments = paginate(request, indictments)

            context = {'form' : form, 'indictments' : indictments,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/indictments-results.html', context)
        
    context = {'form' : form, 'indictments' : PvdmDocs110.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/indictments-results.html', context)


#law&chancery search
def lawChancerySearch(request):
    return createForm(request, 'batches/law-chancery-search.html', LawChanceryForm)


#bond law&chancery display results
def lawChanceryResults(request):
    form = LawChanceryForm()
    if request.method == 'GET':
        form = LawChanceryForm(request.GET)
        if form.is_valid():
            date = form.cleaned_data.get('docindex1', '')
            law_Chancery = form.cleaned_data.get('docindex2', '')


            query = Q()

            if date:
                query &= Q(docindex1=date)
            if law_Chancery:
                query &= Q(docindex2=law_Chancery)


            lawChancery = PvdmDocs16.objects.filter(query) if query else PvdmDocs16.objects.none()

            resultCount = lawChancery.count() if query else 0

            custom_range, lawChancery = paginate(request, lawChancery)

            context = {'form' : form, 'lawChancery' : lawChancery,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/law-chancery-results.html', context)
        
    context = {'form' : form, 'lawChancery' : PvdmDocs16.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/law-chancery-results.html', context)


#destruction orders search
def destructionOrdersSearch(request):
    return createForm(request, 'batches/destruction-orders-search.html', DestructionOrdersForm)


#destruction orders display results
def destructionOrdersResults(request):
    form = DestructionOrdersForm()
    if request.method == 'GET':
        form = DestructionOrdersForm(request.GET)
        if form.is_valid():
            order_type = form.cleaned_data.get('docindex1', '')
            order_date = form.cleaned_data.get('docindex2', '')


            query = Q()

            if order_type:
                query &= Q(docindex1=order_type)
            if order_date:
                query &= Q(docindex2=order_date)


            destructionOrders = PvdmDocs115.objects.filter(query) if query else PvdmDocs115.objects.none()

            resultCount = destructionOrders.count() if query else 0

            custom_range, destructionOrders = paginate(request, destructionOrders)

            context = {'form' : form, 'destructionOrders' : destructionOrders,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/destruction-orders-results.html', context)
        
    context = {'form' : form, 'lawChancery' : PvdmDocs115.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/destruction-orders-results.html', context)


#adoption search
def adoptionSearch(request):
    return createForm(request, 'batches/adoption-search.html', AdoptionForm)


#adoption display results
def adoptionResults(request):
    form = AdoptionForm()
    if request.method == 'GET':
        form = AdoptionForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            plaintiff_last_name = form.cleaned_data.get('docindex6', '')
            plaintiff_first_name = form.cleaned_data.get('docindex7', '')
            subject_last_name = form.cleaned_data.get('docindex16', '')
            subject_first_name = form.cleaned_data.get('docindex17', '')


            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if plaintiff_last_name:
                query &= Q(docindex6=plaintiff_last_name)
            if plaintiff_first_name:
                query &= Q(docindex7=plaintiff_first_name)
            if subject_last_name:
                query &= Q(docindex16=subject_last_name)
            if subject_first_name:
                query &= Q(docindex17=subject_first_name)


            adoption = PvdmDocs14.objects.filter(query) if query else PvdmDocs14.objects.none()

            resultCount = adoption.count() if query else 0

            custom_range, adoption = paginate(request, adoption)

            context = {'form' : form, 'adoption' : adoption,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/adoption-results.html', context)
        
    context = {'form' : form, 'lawChancery' : PvdmDocs14.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/adoption-results.html', context)


#clerk orders search
def clerkOrdersSearch(request):
    return createForm(request, 'batches/clerk-orders-search.html', ClerkOrdersForm)


#clerk orders display results
def clerkOrdersResults(request):
    form = ClerkOrdersForm()
    if request.method == 'GET':
        form = ClerkOrdersForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            plaintiff_company = form.cleaned_data.get('docindex8', '')
            plaintiff_last_name = form.cleaned_data.get('docindex9', '')
            plaintiff_first_name = form.cleaned_data.get('docindex10', '')
            defendant_company = form.cleaned_data.get('docindex13', '')
            defendant_last_name = form.cleaned_data.get('docindex14', '')
            defendant_first_name = form.cleaned_data.get('docindex15', '')
            subject_company = form.cleaned_data.get('docindex18', '')
            subject_last_name = form.cleaned_data.get('docindex19', '')
            subject_first_name = form.cleaned_data.get('docindex20', '')


            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if plaintiff_company:
                query &= Q(docindex8=plaintiff_company)
            if plaintiff_last_name:
                query &= Q(docindex9=plaintiff_last_name)
            if plaintiff_first_name:
                query &= Q(docindex10=plaintiff_first_name)
            if defendant_company:
                query &= Q(docindex13=defendant_company)
            if defendant_last_name:
                query &= Q(docindex14=defendant_last_name)
            if defendant_first_name:
                query &= Q(docindex15=defendant_first_name)
            if subject_company:
                query &= Q(docindex18=subject_company)
            if subject_last_name:
                query &= Q(docindex19=subject_last_name)
            if subject_first_name:
                query &= Q(docindex20=subject_first_name)


            clerkOrder = PvdmDocs18.objects.filter(query) if query else PvdmDocs18.objects.none()

            resultCount = clerkOrder.count() if query else 0

            custom_range, clerkOrder = paginate(request, clerkOrder)

            context = {'form' : form, 'clerkOrder' : clerkOrder,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/clerk-orders-results.html', context)
        
    context = {'form' : form, 'lawChancery' : PvdmDocs18.objects.none(), 'resultCount' : 0}
    return render(request, 'batches/clerk-orders-results.html', context)



def viewImage(request, pk):  
    image = PvdmObjs116.objects.filter(docid=pk).first()
    print('------------------')
    print(image.docid, image.filelist) 
    print('----------------------------------')
 
    if image:
        dg_id = image.dgid
        dg_query = PvdmDg1.objects.filter(dgid=dg_id).first()
        print('--------------------------')
        print(dg_query.path)
        print('---------------------------')
        if dg_query:
            # path = dg_query.path + image.filelist
            path = os.path.join(dg_query.path, image.filelist)

            print('--------------------------')
            print(path)
            print('--------------------------')

            try:
                # with open(path, 'rb') as f:
                #     return FileResponse(f)
                ######################
                # return FileResponse(open(path, 'rb'))
                # with open(path, 'rb') as f:
                #     image_data = base64.b64encode(f.read()).decode('utf-8')
                #     return render(request, 'batches/single-image.html', {'image_data': image_data})
                with Image.open(path) as img:
                    output = io.BytesIO()
                    img.convert("RGB").save(output, format="JPEG")
                    image_data = base64.b64encode(output.getvalue()).decode('utf-8')
                    return render(request, 'batches/single-image.html', {'image_data': image_data})
            except FileNotFoundError:
                # return HttpResponse("Image not found")
                # return HttpResponse("Image not found", status=404)
                return render(request, 'batches/single-image.html', {'image_data': None})
        else:
            # return HttpResponse("Image path not found")
            # return HttpResponse("Image path not found", status=404)
            return render(request, 'batches/single-image.html', {'image_data': None})
    else:
        # return HttpResponse("Image not found")
        # return HttpResponse("Image not found", status=404)
        return render(request, 'batches/single-image.html', {'image_data': None})


# def editImageMetaData(request, pk):
#     data = PvdmObjs116.objects.get(docid=pk)
#     form = UpdateBondBooks(instance=data)

#     if request.method == 'POST':
#         form = UpdateBondBooks(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect('singleImage')
        
#     context = {'form':form}
#     return render(request, 'batches/single-image.html', context)



