from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
