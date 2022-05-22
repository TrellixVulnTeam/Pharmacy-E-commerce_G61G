from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('routers/', include((routers.urls, 'router'))),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('updateItem', views.updateItem, name='updateItem'),
    path('processOrder', views.processOrder, name='processOrder'),
    path('apilogin', views.apilogin, name='apilogin'),
    
]