from django.contrib import admin
from django.urls import path, include
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.category_list, name='home'),
    path('categories/', include('store.urls')), 
]