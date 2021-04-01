from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name='index'),
    path('search_details', views.search_details, name='search_details'),
]
