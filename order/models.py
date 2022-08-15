from django.db import models
from product.models import Product

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_created=True)
    products = models.ManyToManyField(Product)
