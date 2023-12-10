from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request, "shopify/index.html")


def register(request):
    if request.method == "POST":
        return render(request, "shopify/apology.html")
    else:
        return render(request, "shopify/register.html")



def login(request):
    if request.method == "POST":
        return render(request, "shopify/apology.html")
    else:
        return render(request, "shopify/login.html")