from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    phone_number = PhoneNumberField(blank=True)
    additional_info = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ['-created']
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_sum(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderInstance(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta():
        verbose_name = 'Order Instance'
        verbose_name_plural = 'Order Instances'

    def __str__(self):
        return f'OrderInstance {self.id}'

    def get_cost(self):
        return self.price * self.quantity
