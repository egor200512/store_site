from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products import views
from .views import login, UserProfileView, logout, UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
]