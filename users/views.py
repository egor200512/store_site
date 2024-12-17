from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


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
        'form': UserLoginForm
    }
    return render(request, 'users/login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)

