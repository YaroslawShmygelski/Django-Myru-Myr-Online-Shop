# Generated by Django 5.0.3 on 2024-03-28 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name': 'category',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id'], name='shop_catego_id_d67477_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=200)),
                ('code', models.CharField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('created', models.DateField(auto_now_add=True)),
                ('changed', models.DateField(auto_now=True)),
                ('posted', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='products_photo/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
            options={
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id', 'slug'], name='shop_produc_id_f21274_idx'), models.Index(fields=['name'], name='shop_produc_name_a2070e_idx'), models.Index(fields=['price'], name='shop_produc_price_3b79b5_idx')],
            },
        ),
    ]
