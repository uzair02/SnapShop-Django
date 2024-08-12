from django.db import models
from django.utils import timezone

class ScrapedData(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    link = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Scraped Product"
