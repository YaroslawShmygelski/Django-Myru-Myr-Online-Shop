from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from orders.forms import OrderForm
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


def ajax_add_to_cart(request):
    product_id = int(request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product=product,
             quantity=quantity)

    data = {'message': 'succes'}
    return JsonResponse(data)


def remove_from_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart_view')


def cart_view(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

            cart.clear_cart()

        return render(request, 'cart/cart.html', {'cart': cart})

    else:
        form = OrderForm()
        return render(request, 'cart/cart.html', {'cart': cart, 'form': form})


def test_view(request):
    form = CartAddForm()
    if request.method == 'POST':
        test = {'test1': 'test.message'}
        return JsonResponse(test)
    else:
        return render(request, 'cart/Test.html', context={'form': form})
