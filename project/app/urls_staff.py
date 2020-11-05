#app/urls_staff.py
from django.urls import path
from .views_staff import *
urlpatterns = [
  path('', staffHome, name='staff-home'),
  path('list-category', listCategory, name='list-category'),
  path('create-category', CategoryCreateView.as_view(), name='create-category'),
  path('update-category/<pk>', CategoryUpdateView.as_view(), name='update-category'),
  path('delete-category/<pk>', deleteCategory, name='delete-category'),

  path('list-product', listProduct, name='list-product'),
  path('create-product', createProduct, name='create-product'),
  path('update-product/<pk>', updateProduct, name='update-product'),
  path('delete-product/<pk>', deleteProduct, name='delete-product'),
]