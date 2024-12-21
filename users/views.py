from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.template.context_processors import request
from django.urls import reverse

from products.models import Product, Basket
from products.views import basket_remove
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

    baskets = Basket.objects.filter(user=request.user)

    total_price , total_quantity = 0, 0
    for i in baskets:
        total_quantity += i.quantity
        total_price += i.product.price * i.quantity


    context = {
        'title':'Профиль',
        'form':form,
        'baskets':baskets,
        'total_quantity':total_quantity,
        'total_price':total_price,

    }

    return render(request, 'users/profile.html', context=context)

