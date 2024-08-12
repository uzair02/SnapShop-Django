# models.py
from django.utils import timezone
from django.db import models

class SearchResult(models.Model):
    description = models.CharField(max_length=255)
    link = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.description
