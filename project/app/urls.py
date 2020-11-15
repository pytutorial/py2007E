from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('product-detail/<pk>', viewProductDetail),
    path('order-product/<pk>', orderProduct),
    path('thank-you', thank_you),
]