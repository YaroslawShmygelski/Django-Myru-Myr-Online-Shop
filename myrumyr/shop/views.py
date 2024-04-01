from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


def hello_site(request):
    products = Product.objects.all()

    return render(request, 'shop/index.html', {'products': products})


def show_product(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'shop/single-product.html', {'product': product})

