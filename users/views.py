from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from mixins.views import TitleMixin
from users.models import User
from products.models import Product, Basket
from products.views import basket_remove
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


class UserLoginView(TitleMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'Авторизация'

class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались'
    title = 'Регистрация'

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        return context


class UserProfileView(TitleMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    title = 'Профиль'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))