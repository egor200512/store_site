from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products import views
from products.views import products, basket_add, basket_remove


app_name = 'products'
urlpatterns = [
    path('', products, name='index'),
    path('category/<int:cat_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/del/<int:basket_id>/', basket_remove, name='basket_del'),
]
