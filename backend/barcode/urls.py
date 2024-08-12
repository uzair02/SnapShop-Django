from django.urls import path
from .views import decode_barcode

urlpatterns = [
    path('decode-barcode/', decode_barcode, name='decode_barcode'),
]
