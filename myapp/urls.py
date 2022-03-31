from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('shopsingle', views.shopsingle, name='shopsingle')
    
]