from django.urls import path
from . import views


urlpatterns =[
    path('', views.landingBatches, name="landingBatches"),
    path('delete-Batch/', views.deleteBatch, name="deleteBatch"),
    path('filling-Batch/', views.fillingBatch, name="fillingBatch"),
    path('incomplete-Batch/', views.incompleteBatch, name="incompleteBatch"),
    path('update-Batch/', views.updateBatch, name="updateBatch"),
    path('single-Batch/', views.singleBatch, name="singleBatch"),
    path('civil-Search/', views.civilSearch, name="civilSearch"),
    path('criminal-Cases-Search/', views.criminalCasesSearch, name="criminalCasesSearch"),
    path('criminal-Juvenile-Search/', views.criminalJuvenileSearch, name="criminalJuvenileSearch"),
    path('criminal-Search/', views.criminalSearch, name="criminalSearch"),
    path('historic-Index-Cards-Search/', views.historicIndexCardsSearch, name="historicIndexCardsSearch"),
    path('historic-Order-Books-Search/', views.historicOrderBooksSearch, name="historicOrderBooksSearch"),
    path('hr-Search/', views.hrSearch, name="hrSearch"),
    path('scanner-setting/', views.scannerSetting, name="scannerSetting"),
    path('new-batch/', views.newBatch, name="newBatch"),
    path('capture/', views.capture, name="capture"),

]