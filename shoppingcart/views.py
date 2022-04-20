
from django.shortcuts import render
from store.models import Cart, CartItem, Product


def home(request):
    products = Product.objects.all()
    carts = CartItem.objects.filter(cart_id=1)

    context = {
        'products': products,
        'carts': carts
    }

    return render(request, 'home.html', context=context)