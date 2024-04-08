from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def index_view(request):
    products = Product.objects.all()

    return render(request, 'shop/index.html', {'products': products})


def show_single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'shop/single-product.html', {'product': product})


def show_catalog(request):
    products = Product.objects.all()

    return render(request, 'shop/catalog.html', {'products': products})



def cart_view(request):

    return render(request, 'shop/cart.html')
