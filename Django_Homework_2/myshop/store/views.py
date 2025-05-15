# store/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Avg, Max, Min, Sum


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def category_detail(request, category_id):
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
    return render(request, 'store/category_detail.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})
