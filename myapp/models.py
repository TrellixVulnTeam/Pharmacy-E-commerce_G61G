from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, default='My product name')
    details = models.TextField(default='My products details')
    img = models.ImageField(upload_to = "products/%y", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default='45')
    prod_prop = models.CharField(max_length=50, default='supplement')
    