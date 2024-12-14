from django.urls import path
from . import views



urlpatterns =[
    path('', views.landingBatches, name="landingBatches"),
    path('general_search/', views.general_search, name="generalResults"),
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
    path('concealed-weapons-search/', views.ConcealedWeaponsSearch, name="ConcealedWeaponsSearch"),
    path('concealed-weapons-results/', views.ConcealedWeaponsResults, name="ConcealedWeaponsResults"),
    path('charters-Search/', views.chartersSearch, name="chartersSearch"),
    path('charters-results/', views.chartersResults, name="chartersResults"),
    path('indictments-search/', views.indictmentsSearch, name="indictmentsSearch"),
    path('indictments-results/', views.indictmentsResults, name="indictmentsResults"),
    path('law-chancery-results/', views.lawChanceryResults, name="lawChanceryResults"),
    path('law-chancery-search/', views.lawChancerySearch, name="lawChancerySearch"),
    path('destruction-orders-search/', views.destructionOrdersSearch, name="destructionOrdersSearch"),
    path('destruction-orders-results/', views.destructionOrdersResults, name="destructionOrdersResults"),
    path('adoption-search/', views.adoptionSearch, name="adoptionSearch"),
    path('adoption-results/', views.adoptionResults, name="adoptionResults"),
    path('clerk-orders-search/', views.clerkOrdersSearch, name="clerkOrdersSearch"),
    path('clerk-orders-results/', views.clerkOrdersResults, name="clerkOrdersResults"),
    path('single-image/<str:section>/<str:pk>/', views.single_image_view, name="singleImage"),
    path('section-results/', views.view_section_results, name='sectionResults'),
    path('export/', views.export_table, name='export_table'),
   
]
