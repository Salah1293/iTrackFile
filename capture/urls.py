from django.urls import path
from . import views


urlpatterns =[
    path('create-batch/', views.create_batch, name="createBatch"),
    path('upload-images/', views.upload_images, name='upload_images'),
    path('upload-scanned-images/', views.upload_scanned_images, name='upload_scanned_images'),
    path('new-batch/', views.new_batch, name="newBatch"),
    path('', views.capture, name="capture"),
    path('incomplete-batch/', views.incomplete_batch_list, name="incompleteBatch"),
    path('delete-image/', views.delete_image, name='delete_image'),
    path('update-batches/<str:pk>/', views.update_batch, name='updateBatches'),
    path('create-bundle/', views.create_bundle, name='create_bundle'),
    path('submit-bundle/', views.submit_bundle, name='submit_bundle'),
    path('bundle-data/<str:bundleid>/<str:batchid>/', views.get_bundle_data, name='get_bundle_data'),

]