from django.db import models

# Create your models here.
class Customer(models.Model):
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
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField( auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True)