# store/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import Avg
from .forms import ProductForm, CategoryForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView




from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy, reverse
from django.db.models import Avg
from .models import Category, Product
from .forms import ProductForm, CategoryForm



class BaseView(TemplateView):
    template_name = 'store/base.html'



class CategoryListView(ListView):
    model = Category
    template_name = 'store/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(View):
    template_name = 'store/category_detail.html'

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = category.products.all()

        avg_price = products.aggregate(avg=Avg('price'))['avg']
        max_product = products.order_by('-price').first()
        min_product = products.order_by('price').first()
        total_value = sum(p.price * p.quantity for p in products)

        context = {
            'category': category,
            'avg_price': avg_price,
            'total_value': total_value,
            'products': products,
            'max_product': max_product,
            'min_product': min_product,
        }
        return render(request, self.template_name, context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return self.category.products.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/add_product.html'
    success_url = reverse_lazy('category_list')


class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/update_product.html'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'store/delete_product.html'
    success_url = reverse_lazy('category_list')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'store/add_category.html'
    success_url = reverse_lazy('category_list')


from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('category_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'store/login.html'
