from django.urls import path
from . import views


urlpatterns =[
    path('help/', views.help_app, name='help'),
    path('', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('myuser/', views.myUser, name='myUser'),
    path('myadmin/', views.myAdmin, name='myAdmin'),
    path('managing/', views.managing, name='managing'),
    path('user_list/', views.user_list, name='userList'),
    path('create_user/', views.create_user, name='createUser'),
    path('update-user/<int:user_id>/', views.update_user, name='updateUser'),
    path('delete-user/<int:user_id>/', views.delete_user, name='deleteUser'),
    # path('update-profile/', views.update_profile_self, name='update_profile_self'),

]