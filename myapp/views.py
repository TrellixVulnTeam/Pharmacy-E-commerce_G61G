from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        
        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    products = Product.objects.all()
    
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    products = Product.objects.all()
    product_paginator = Paginator(products, 9)
    page_num = request.GET.get('page', 1)
    page = product_paginator.get_page(page_num)
    
    return render(request, 'shop.html', {'products': page})

@login_required(login_url='login')
def product_details(request, id):
    #Fetching product using id
    products = Product.objects.filter(id=id)
    return render(request, 'product_details.html', {'products': products})

@login_required(login_url='login')
def thankyou(request):
    return render(request, 'product_details.html')



