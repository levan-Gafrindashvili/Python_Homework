# store/urls.py

from django.urls import path
from .views import (
    BaseView, CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView, AddProductView,
    UpdateProductView, DeleteProductView, AddCategoryView,
)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:category_id>/products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/edit/', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('category/add/', AddCategoryView.as_view(), name='add_category'),
]
