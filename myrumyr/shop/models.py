from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    code = models.CharField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300, blank=True)
    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)
    posted = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products_photo/%Y/%m/%d', blank=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:single-product', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'cat_slug': self.slug})
