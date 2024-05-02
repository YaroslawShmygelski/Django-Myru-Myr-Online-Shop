from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddForm


# Create your views here.


def index_view(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


def show_single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_form=CartAddForm()

    return render(request, 'shop/single-product.html', {'product': product, 'cart_form': cart_form})


def get_category_products(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/catalog.html', {'products': products})


def show_catalog(request):
    products = Product.objects.all()
    cart_form = CartAddForm()

    return render(request, 'shop/catalog.html', {'products': products, 'form':cart_form})


def cart_view(request):
    return render(request, 'shop/cart.html')


def contact_view(request):
    return render(request, 'shop/contact.html')
