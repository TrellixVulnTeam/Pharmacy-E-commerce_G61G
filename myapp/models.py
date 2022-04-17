from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField( auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Pain Relief', 'Pain Relief'),
        ('Oral Care', 'Oral Care'),
        ('First Aid', 'First Aid'),
        ('Vitamins & Minerals', 'Vitamins & Minerals'),
        ('Stomach & Bowel', 'Stomach & Bowel'),
        ('Cough, Cold & Flu', 'Cough, Cold & Flu'),
        ('Allergy & Hayfever', 'Allergy & Hayfever'),
        ('Sexual Health', 'Sexual Health'),
    )
    
    name = models.CharField(max_length=200, default='product name')
    description = models.TextField(max_length=6000, default='product description')
    image = models.ImageField(upload_to = "img/%y", null=True)
    price = models.FloatField(default='0.00')
    category = models.CharField(max_length=200, default='Not provided', choices=CATEGORY)
    date_created = models.DateTimeField( auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)
        
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
    )
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL, blank=True)
    date_created = models.DateTimeField( auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    status = models.CharField(max_length=200, null=True)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            shipping = True
        
        return shipping
 
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL, blank=True)
    order = models.ForeignKey(Order, null=True, on_delete= models.SET_NULL, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField( auto_now_add=True, null=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL, blank=True)
    order = models.ForeignKey(Order, null=True, on_delete= models.SET_NULL, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField( auto_now_add=True, null=True)
    
    def __str__(self):
        return self.address
    
    