from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
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
    items = Item.objects.all()
    
    return render(request, 'index.html', {'items': items})

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
    return render(request, 'shop.html')

@login_required(login_url='login')
def shopsingle(request):
    return render(request, 'shopsingle.html')

@login_required(login_url='login')
def thankyou(request):
    return render(request, 'shopsingle.html')



