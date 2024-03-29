from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.


def hello_site(request):
    products = Product.objects.all()

    return render(request, 'shop/index.html', {'products': products})
