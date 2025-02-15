from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from products import views
from products.views import ProductsListView, basket_add, basket_remove

app_name = 'products'
urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:cat_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/del/<int:basket_id>/', basket_remove, name='basket_del'),
]
