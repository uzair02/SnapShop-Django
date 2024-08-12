from django.db import models
from django.conf import settings

class WebStore(models.Model):
    title = models.CharField(max_length=200)
    webstore_name = models.CharField(max_length=150)
    price = models.CharField(max_length=20, blank=True, null=True) 
    link = models.URLField()

class WebStoreRating(models.Model):
    webstore = models.CharField(max_length=150)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)