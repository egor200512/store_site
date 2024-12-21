from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products import views
from products.views import products, basket_add


app_name = 'products'
urlpatterns = [
    path('', products, name='index'),
    path('basket/add/<int:product_id>', basket_add, name='basket_add'),
]
