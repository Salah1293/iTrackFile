from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

    
