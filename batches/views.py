from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .utils import *
from .forms import *


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

            
            if query:
                criminal = PvdmDocs11.objects.filter(query)
            else:
                criminal = PvdmDocs11.objects.none()
                

            

            context = {'form': form, 'criminal': criminal, 'resultCount' : criminal.count()}
            return render(request, 'batches/criminal-results.html', context)

    context={'form' : form, 'criminal' : PvdmDocs11.objects.none()}    
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

           
            # query = Q()

            # if case_number:
            #     query &= Q(docindex1=case_number)
            # if start_date and end_date:
            #     query &= Q(docindex2__range=[start_date, end_date])
            # if last_name:
            #     query &= (Q(docindex11=last_name) | Q(docindex6=last_name))
            # if first_name:
            #     query &= (Q(docindex12=first_name) | Q(docindex7=first_name))

            
            # if query:
            #     civil = PvdmDocs12.objects.filter(query)
            # else:
            #     civil = PvdmDocs12.objects.none()


            query = Q()

            if case_number:
                query &= Q(docindex1=case_number)
            if start_date and end_date:
                query &= Q(docindex2__range=[start_date, end_date])

            if last_name or first_name:
                name_query = Q()
                if last_name:
                    name_query |= Q(docindex11=last_name) | Q(docindex6=last_name)
                if first_name:
                    name_query |= Q(docindex12=first_name) | Q(docindex7=first_name)
                query &= name_query

            if query:
                civil = PvdmDocs12.objects.filter(query)
            else:
                civil = PvdmDocs12.objects.none()

            context = {'form': form, 'civil': civil, 'resultCount' : civil.count()}
            return render(request, 'batches/civil-results.html', context)
        
    
    context={'form' : form, 'civil' : PvdmDocs12.objects.none()}    
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

            
            if query:
                criminalCases = PvdmDocs15.objects.filter(query)
            else:
                criminalCases = PvdmDocs15.objects.none()

            context = {'form': form, 'criminalCases': criminalCases, 'resultCount' : criminalCases.count()}
            return render(request, 'batches/criminal-cases-results.html', context)
        
    
    context={'form' : form, 'criminalCases' : PvdmDocs17.objects.none()}    
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

            
            if query:
                ciminalJuvenile = PvdmDocs15.objects.filter(query)
            else:
                ciminalJuvenile = PvdmDocs15.objects.none()

            context = {'form' : form,'ciminalJuvenile' : ciminalJuvenile, 'resultCount' : ciminalJuvenile.count()}
            return render(request, 'batches/criminal-juvenile-results.html', context)
        
    
    context={'form' : form, 'ciminalJuvenile' : PvdmDocs13.objects.none()}    
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

            
            if query:
                historicIndexCards = PvdmDocs15.objects.filter(query)
            else:
                historicIndexCards = PvdmDocs15.objects.none()

            context = {'form' : form, 'historicIndexCards': historicIndexCards, 'resultCount' : historicIndexCards.count()}
            return render(request, 'batches/historic-index-cards-results.html', context)
        

    context = {'form' : form, 'historicIndexCards' : PvdmDocs114.objects.none()}
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

            if query:
                historicOrderBooks = PvdmDocs15.objects.filter(query)
            else:
                historicOrderBooks = PvdmDocs15.objects.none()

            context = {'form' : form, 'historicOrderBooks' : historicOrderBooks, 'resultCount' : historicOrderBooks.count()}
            return render(request, 'batches/historic-order-books-results.html', context)

    context = {'form' : form, 'historicOrderBooks' : PvdmDocs113.objects.none()}
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

                
            if query:
                hr = PvdmDocs15.objects.filter(query)
            else:
                hr = PvdmDocs15.objects.none()

            context = {'form' : form, 'hr' : hr, 'resultCount' : hr.count()}
            return render(request, 'batches/hr-results.html', context)
        

    context = {'form' : form, 'hr' : PvdmDocs15.objects.none()}
    return render(request, 'batches/hr-results.html', context)