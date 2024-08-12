from rest_framework import serializers
from .models import WebStoreRating

class WebStoreRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebStoreRating
        fields = ['webstore', 'rating', 'review', 'user']
