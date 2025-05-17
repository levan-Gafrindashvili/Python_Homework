# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<int:category_id>/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
