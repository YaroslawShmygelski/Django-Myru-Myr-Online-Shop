from decimal import Decimal

from django.conf import settings

from shop.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}

        self.cart[product_id]['quantity'] = quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        self.product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=self.product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
            cart[str(product.id)]['price']=int(product.price)

        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        res = 0
        for item in self.cart.values():
            res += (item['quantity'])
        return res

    def get_total_sum(self):
        res = 0
        for item in self.cart.values():
            res += Decimal((item['quantity'] * item['price']))
        return res

    def clear_cart(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
