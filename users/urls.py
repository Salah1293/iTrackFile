from django.urls import path
from . import views


urlpatterns =[
    path('help/', views.help, name='help'),
    path('login/', views.login, name='login'),
    path('myuser/', views.myUser, name='myUser'),
    path('myadmin/', views.myAdmin, name='myAdmin'),
]