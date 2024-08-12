# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy


# class ProductsItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

from scrapy_djangoitem import DjangoItem
from pro_scrape.models import ScrapedData

class ScrapedDataItem(DjangoItem):
    django_model = ScrapedData