from django.shortcuts import render

from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title' : 'Главная страница',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title' : 'Товары',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)