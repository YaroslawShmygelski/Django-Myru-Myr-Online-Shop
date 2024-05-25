from django.http import  JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from orders.forms import OrderForm
from orders.models import OrderInstance
from orders.tasks import order_create_send_email, order_send_pdf_order, test_task
from .cart import Cart
from .forms import CartAddForm
from shop.models import Product



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
    test_task.delay()
    cart = Cart(request)

    # Processing order validation
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderInstance.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
            cart.clear_cart()
            order_create_send_email.delay(order.id)
            order_send_pdf_order.delay(order.id)
            test_task.delay()
            url_with_params = reverse('cart:cart_view') + '?success_form=true'
            return redirect(url_with_params)
        else:
            return render(request, 'cart/cart.html', {'form': form})


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
