from django.shortcuts import render

# Create your views here.





def deleteBatch (request):

    return render(request , 'batches/delete-batch.html')



def updateBatch (request):

    return render(request , 'batches/update-batch.html')


def incompleteBatch (request):

    return render(request , 'batches/incomplete-batches.html')


def fillingBatch (request):

    return render(request , 'batches/filling-batch.html')


def landingBatches (request):

    return render(request , 'batches/landing-page.html')


def singleBatch (request):

    return render(request , 'batches/single-batch.html')


def civilSearch (request):

    return render(request , 'batches/civil-Search.html')


def criminalCasesSearch (request):

    return render(request , 'batches/criminal-Cases-Search.html')


def criminalJuvenileSearch (request):

    return render(request , 'batches/criminal-Juvenile-Search.html')


def criminalSearch (request):

    return render(request , 'batches/criminal-Search.html')


def historicIndexCardsSearch (request):

    return render(request , 'batches/hisoric-index-cards-search.html')


def historicOrderBooksSearch (request):

    return render(request , 'batches/historic-Order-Books-Search.html')


def hrSearch (request):

    return render(request , 'batches/hr-Search.html')


def newBatch (request):

    return render(request , 'batches/new-batch.html')


def scannerSetting (request):

    return render(request , 'batches/scanner-setting.html')


def capture (request):

    return render(request , 'batches/capture.html')