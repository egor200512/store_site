from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products import views
from .views import UserProfileView, UserRegistrationView, UserLoginView, EmailVerificationView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]