from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    slug = models.SlugField(max_length=200)
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

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id'])
        ]
        verbose_name = 'category'

    def __str__(self):
        return self.name
