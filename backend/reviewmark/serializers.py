from rest_framework import serializers
from .models import Wishlist, ProductReview

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['user', 'product']

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['user', 'product', 'rating', 'review']
