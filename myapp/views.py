from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    items = Item.objects.all()
    
    return render(request, 'index.html', {'items': items})

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def shopsingle(request):
    return render(request, 'shopsingle.html')

def thankyou(request):
    return render(request, 'shopsingle.html')



