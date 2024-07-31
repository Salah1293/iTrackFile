from django.urls import path
from . import views


urlpatterns =[
    path('create-batch/', views.create_batch, name="createBatch"),
    path('upload-images/', views.upload_images, name='upload_images'),
    path('upload_scanned_images/', views.upload_scanned_images, name='upload_scanned_images'),
    path('new-batch/', views.new_batch, name="newBatch"),
    path('', views.capture, name="capture"),
    path('incomplete-batch/', views.incompleteBatch, name="incompleteBatch"),

]