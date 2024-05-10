from django.contrib import admin

from orders.models import Order, OrderInstance


class OrderInstanceInline(admin.TabularInline):
    model = OrderInstance
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'city', 'created', 'updated']
    list_filter = ['created', 'updated', 'last_name']
    inlines = [OrderInstanceInline]
