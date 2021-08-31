from django.urls import path
from searchmovies import views

app_name = 'searchapp'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('search/', views.searchView, name='search'),
    path('search_history/', views.searchHistoryView, name='search-history'),
    path('filter/', views.filter_data, name='filter'),
]