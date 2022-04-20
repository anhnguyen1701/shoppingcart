from tkinter import CASCADE
from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    user = 'lamanh'
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def sub_total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.product_name
