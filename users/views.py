from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse

from products.models import Product, Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        context = {
            'title':'Профиль',
            'form':form,
            'baskets':Basket.objects.filter(user=request.user)
        }
        return render(request, 'users/profile.html', context)

