from django.contrib import admin

from .models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created', 'changed', 'category', 'posted']
    list_filter = ['posted', 'created', 'changed']
    list_editable = [ 'price', 'posted']
    prepopulated_fields = {'slug': ('name',)}