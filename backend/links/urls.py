from django.urls import path
from .views import *  

urlpatterns = [
    path('search_and_store/', search_and_store, name='search_and_store'),
    path('get_products/', get_products, name='get_products'),
    path('get_scraped_products/', get_scraped_products, name='get_scraped_products'),

]
