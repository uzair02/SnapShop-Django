# urls.py (inside your app)

from django.urls import path
from . import views

urlpatterns = [
    path('submit_rating/', views.submit_rating, name='submit_rating'),
    path('webstore_names/', views.get_webstore_names, name='get_webstore_names'),
    path('webstore_ratings/', views.get_webstore_ratings, name='webstore_ratings'),
    path('webstores/', views.get_product_details, name='webstore_detail'),
    path('recommendations/', views.recommend_products, name='recommend_products_api'),
]
