from django.urls import path
from . import views


urlpatterns =[
    path('', views.landingBatches, name="landingBatches"),
    path('delete-batch/', views.deleteBatch, name="deleteBatch"),
    path('filling-batch/', views.fillingBatch, name="fillingBatch"),
    path('incomplete-batch/', views.incompleteBatch, name="incompleteBatch"),
    path('update-batch/', views.updateBatch, name="updateBatch"),
    path('single-batch/', views.singleBatch, name="singleBatch"),
    path('civil-search/', views.civilSearch, name="civilSearch"),
    path('civil-results/', views.civilResults, name="civilResults"),
    path('criminal-cases-search/', views.criminalCasesSearch, name="criminalCasesSearch"),
    path('criminal-cases-results/', views.criminalCasesResults, name="criminalCasesResults"),
    path('criminal-juvenile-search/', views.criminalJuvenileSearch, name="criminalJuvenileSearch"),
    path('criminal-juvenile-results/', views.criminalJuvenileResults, name="criminalJuvenileResults"),
    path('criminal-search/', views.criminalSearch, name="criminalSearch"),
    path('criminal-results/', views.criminalResults, name="criminalResults"),
    path('historic-index-cards-search/', views.historicIndexCardsSearch, name="historicIndexCardsSearch"),
    path('historic-index-cards-results/', views.historicIndexCardsResults, name="historicIndexCardsResults"),
    path('historic-order-books-search/', views.historicOrderBooksSearch, name="historicOrderBooksSearch"),
    path('historic-order-books-results/', views.historicOrderBooksResults, name="historicOrderBooksResults"),
    path('hr-search/', views.hrSearch, name="hrSearch"),
    path('hr-results/', views.hrResults, name="hrResults"),
    path('bond-search/', views.bondBooksSearch, name="bondBooksSearch"),
    path('bond-results/', views.bondBooksResults, name="bondBooksResults"),
    path('scanner-setting/', views.scannerSetting, name="scannerSetting"),
    path('new-batch/', views.newBatch, name="newBatch"),
    path('capture/', views.capture, name="capture"),

]