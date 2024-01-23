from django.shortcuts import render

# Create your views here.


def login(request):

    return render(request, 'users/login.html')


def myAdmin(request):

    return render(request, 'users/admin.html')


def help(request):

    return render(request, 'users/help.html')


def myUser(request):

    return render(request, 'users/user.html')

