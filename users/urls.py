from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products import views
from .views import login, register, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]