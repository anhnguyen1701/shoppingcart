from shoppingcart import views
from django.shortcuts import redirect, render

from store.models import Cart, CartItem, Product

# Create your views here.

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(id = 1)

    cart_item = CartItem.objects.create(
        product = product,
        cart = cart,
        quantity = 1
    )

    cart_item.save()

    return redirect(views.home)