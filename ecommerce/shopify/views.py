from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import Register_Form, Login_Form
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def apology(request):
    return render(request, "shopify/apology.html")


@login_required
def index(request):
    return render(request, "shopify/index.html")


def register(request):
    if request.method == "POST":
        form = Register_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('index')
        else:
            error = form.non_field_errors()
            form = Register_Form()
            return render(request, "shopify/register.html", {'form': form, 'message': error[0], 'message_tag': 'error'})
    else:
        form = Register_Form()
        return render(request, 'shopify/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('index')
        else:
            error = form.non_field_errors()
            form = Login_Form()
            return render(request, 'shopify/login.html', {'form': form, 'message': error[0], 'message_tag': 'error'})
    else:
        form = Login_Form()
        return render(request, 'shopify/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
