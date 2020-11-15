#app/urls_staff.py
from django.urls import path
from .views_staff import *
urlpatterns = [
  #path('', staffHome, name='staff-home'),
  #127.0.0.1:8000/staff --> staff.myshop.com
  path('', listCategory, name='staff-home'),
  path('create-category', CategoryCreateView.as_view(), name='create-category'),
  path('update-category/<pk>', CategoryUpdateView.as_view(), name='update-category'),
  path('delete-category/<pk>', deleteCategory, name='delete-category'),

  path('list-product', listProduct, name='list-product'),
  path('create-product', ProductCreateView.as_view(), name='create-product'),
  path('update-product/<pk>', ProductUpdateView.as_view(), name='update-product'),
  path('delete-product/<pk>', deleteProduct, name='delete-product'),

  path('list-order', listOrder, name='list-order'),
  path('view-order/<pk>', viewOrder, name='view-order'),
]