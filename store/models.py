from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name