from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *


def searchCivil(request):

    form = CivilForm()

    if request.method == 'GET':
        form = CivilForm(request.GET)
        if form.is_valid():
            case_number = form.cleaned_data.get('docindex1', '')
            order_date = form.cleaned_data.get('docindex2', '')
            defenfant_last_name = form.cleaned_data.get('docindex11', '')
            defenfant_first_name = form.cleaned_data.get('docindex12', '')

            civil = PvdmDocs12.objects.filter(
                Q(docindex1=case_number) |
                Q(docindex2=order_date) |
                Q(docindex11=defenfant_last_name) |
                Q(docindex12=defenfant_first_name)
            )

            
    return form, civil





# if request.GET.get('case_namber' | 'defendant_last_name' |
#         'defendant_first_name'):
#         case_namber = request.GET.get('case_namber')
#         defendant_last_name = request.GET.get('defendant_last_name')
#         defendant_first_name = request.GET.get('defendant_first_name')
       
#     criminal = PvdmDocs11.objects.distinct().filter(Q(docindex1 = case_namber) |
#                                          Q(docindex7 = defendant_first_name) |
#                                          Q(docindex6 = defendant_last_name))