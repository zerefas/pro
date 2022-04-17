from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name ='HomeList'),
    path('movie', MovieList.as_view(), name='MovieList'),
    path('category/<str:category>/', MovieCategory.as_view(), name='MovieCategory'),
    path('language/<str:language>/', MovieLanguage.as_view(), name='MovieLanguage'),
    path('search/', MovieSearch.as_view(), name='MovieSearch'),
    path('year/<int:year>/', MovieYear.as_view(), name='MovieYear'),
    path('details/<slug:slug>/', MovieDetails.as_view(), name='MovieDetails')
]