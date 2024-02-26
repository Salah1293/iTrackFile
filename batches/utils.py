from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#pagination super class
def paginate(request, query):
    page = request.GET.get('page')
    result = 25
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

