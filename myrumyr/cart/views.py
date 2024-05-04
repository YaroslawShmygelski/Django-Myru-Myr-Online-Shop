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
        product = get_object_or_404(Product, slug=product_slug)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'])

    return redirect('cart:cart_view')


def remove_from_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart_view')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})


def test_view(request):
    form=CartAddForm()
    return render(request, 'cart/Test.html', context={'form':form} )
