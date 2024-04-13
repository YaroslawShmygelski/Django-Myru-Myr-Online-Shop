
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import CartAddForm
from shop.models import Product


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the")


def add_to_cart(request, product_slug):
    if request.method == "POST":
        form = CartAddForm(request.POST)
        cart = Cart(request)
        products = get_object_or_404(Product, slug=product_slug)
        if form.is_valid():
            cart.add(product=products,
                     quantity=form.changed_data['quantity'])

    return redirect('cart:cart_details')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'templates/cart.html', {'cart':cart})
