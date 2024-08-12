from django.urls import path
from . import views

urlpatterns = [
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('submit_product_review/', views.submit_product_review, name='submit_product_review'),
    path('remove_from_wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('get_wishlist/', views.get_wishlist, name='get_wishlist'),
    path('get_wishlist_items/', views.get_wishlist_items, name='get_wishlist_items'),
    path('get_user_reviews/', views.get_user_reviews, name='get_user_reviews'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]
