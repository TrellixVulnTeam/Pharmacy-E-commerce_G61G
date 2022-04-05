from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
    return render(request, 'cart.html')

@login_required(login_url='login')
def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

@login_required(login_url='login')
def product_details(request, id):
    #Fetching product using id
    products = Product.objects.filter(id=id)
    return render(request, 'product_details.html', {'products': products})

@login_required(login_url='login')
def thankyou(request):
    return render(request, 'product_details.html')



