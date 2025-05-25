# store/urls.py

from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .views import (
    BaseView, CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView, AddProductView,
    UpdateProductView, DeleteProductView, AddCategoryView, CustomLoginView, register_view
)

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:category_id>/products/', ProductListView.as_view(), name='product_list'),
    path('category/add/', AddCategoryView.as_view(), name='add_category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/edit/', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
]

