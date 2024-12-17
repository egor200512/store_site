from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products import views
from .views import login, register

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]