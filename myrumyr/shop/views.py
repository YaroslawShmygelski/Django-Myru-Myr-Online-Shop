from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_site(request):
    return render(request,'shop/index.html')
