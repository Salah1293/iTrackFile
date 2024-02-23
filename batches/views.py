from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .utils import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

def singleBatch (request):

    return render(request , 'batches/single-batch.html')

def newBatch (request):

    return render(request , 'batches/new-batch.html')

def scannerSetting (request):

    return render(request , 'batches/scanner-setting.html')

def capture (request):

    return render(request , 'batches/capture.html')

#criminal search
def criminalSearch(request):
    form = CriminalForm()
    context = {'form': form}
    return render(request, 'batches/criminal-search.html', context)

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
    form = CivilForm()
    context = {'form':form}
    return render(request , 'batches/civil-search.html', context)


#civil display resylts
def civilResults (request):
    form = CivilForm()

    if request.method == 'GET':
        form = CivilForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            # defendant_last_name = form.cleaned_data.get('docindex11', '')
            # defendant_first_name = form.cleaned_data.get('docindex12', '')
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
                query &= (Q(docindex11=last_name) | Q(docindex6=last_name))
            if first_name:
                query &= (Q(docindex12=first_name) | Q(docindex7=first_name))


            civil = PvdmDocs12.objects.filter(query) if query else PvdmDocs12.objects.none()

            resultCount = civil.count() if query else 0

            custom_range, civil = paginate(request, civil)


            # query = Q()

            # if case_number:
            #     query &= Q(docindex1=case_number)
            # if start_date and end_date:
            #     query &= Q(docindex2__range=[start_date, end_date])

            # if last_name or first_name:
            #     name_query = Q()
            #     if last_name:
            #         name_query |= Q(docindex11=last_name) | Q(docindex6=last_name)
            #     if first_name:
            #         name_query |= Q(docindex12=first_name) | Q(docindex7=first_name)
            #     query &= name_query

            # if query:
            #     civil = PvdmDocs12.objects.filter(query)
            # else:
            #     civil = PvdmDocs12.objects.none()

            context = {'form': form, 'civil': civil,
                        'resultCount' : resultCount,
                         'custom_range' : custom_range}
            return render(request, 'batches/civil-results.html', context)
        
    
    context={'form' : form, 'civil' : PvdmDocs12.objects.none(), 'resultCount' : 0}    
    return redirect('civilResults')


#criminal cases search
def criminalCasesSearch (request):
    form = CriminalCasesForm()
    context = {'form': form}
    return render(request , 'batches/criminal-cases-search.html', context)


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
    form = CriminalJuvenileForm()
    context = {'form': form}
    return render(request , 'batches/criminal-juvenile-Search.html', context)


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
    form = HistoricIndexCardsForm()
    context = {'form' : form}
    return render(request , 'batches/hisoric-index-cards-search.html', context)


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
    form = HistoricOrderBooksForm()
    context = {'form' : form}
    return render(request, 'batches/historic-order-books-Search.html', context)


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
    form = HrForm()
    context = {'form' : form}
    return render(request, 'batches/hr-search.html', context)


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
    form = BondBooksForm()
    context = {'form' : form}
    return render(request, 'batches/bond-books-search.html', context)


#bond books display results
def bondBooksResults(request):
    form = BondBooksForm()
    if request.method == 'GET':
        form = HrForm(request.GET)
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
    form = ChartersForm()
    context = {'form' : form}
    return render(request, 'batches/charters-search.html', context)

#charters display results
def chartersResults(request):
    form = ChartersForm()
    if request.method == 'GET':
        form = HrForm(request.GET)
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
    form = ConcealedWeaponsForm()
    context = {'form' : form}
    return render(request, 'batches/concealed-weapons-search.html', context)


#concealed weapons display results
def ConcealedWeaponsResults(request):
    form = ConcealedWeaponsForm()
    if request.method == 'GET':
        form = HrForm(request.GET)
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
    form = IndictmentsForm()
    context = {'form' : form}
    return render(request, 'batches/indictments-search.html', context)


#indictmenys display results
def indictmentsResults(request):
    form = ConcealedWeaponsForm()
    if request.method == 'GET':
        form = HrForm(request.GET)
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
    form = LawChanceryForm()
    context = {'form' : form}
    return render(request, 'batches/law-chancery-search.html', context)


#bond law&chancery display results
def lawChanceryResults(request):
    form = LawChanceryForm()
    if request.method == 'GET':
        form = HrForm(request.GET)
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