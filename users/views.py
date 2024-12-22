from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.models import User
from products.models import Product, Basket
from products.views import basket_remove
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = UserLoginForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'users/login.html', context=context)

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

class UserRegistrationView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Регистрация'
        return context
#             messages.success(request, 'Вы успешно зарегистрировались!')


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Профиль'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))