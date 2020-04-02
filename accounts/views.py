from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')


def logout(request):
    """log the user out"""
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out!')
    return redirect(reverse('index'))


def login(request):
    """ Return a Login page"""
    return render(request, 'login.html')