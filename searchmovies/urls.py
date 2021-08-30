from django.urls import path
from searchmovies import views

app_name = 'searchapp'

urlpatterns = [
    path('', views.indexview, name='index'),
    path('search/', views.searchview, name='search'),
]