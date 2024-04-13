from django.conf import settings

from shop.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            self.cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = product.id
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = product.id
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        self.product_ids = self.cart.keys()
        products = Product.objects.filter(pk__in=self.product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[product.id]['product'] = product
        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        for item in self.cart.values():
            sum += sum(item['quantity'])
        return sum

    def get_total_sum(self):
        for item in self.cart.values():
            sum += sum(item['quantity'] * item['price'])


    def clear_cart(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()