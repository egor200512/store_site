from audioop import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Product, ProductCategory, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


def products(request, cat_id=None, page_number=1):
    product = Product.objects.filter(category_id=cat_id) if cat_id else Product.objects.all()
    paginator = Paginator(object_list=product, per_page=3)
    product_paginator = paginator.page(page_number)

    context = {
        'title' : 'Товары',
        'products': product_paginator,
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.last()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

