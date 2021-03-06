# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-10 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gypsumProducts', '0003_auto_20180809_2331'),
        ('orders', '0004_auto_20180809_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(default=None, max_length=128)),
                ('nmb', models.IntegerField(default=1)),
                ('price_pre_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gypsumProducts.GypsumProduct')),
            ],
            options={
                'verbose_name': 'Товар в корзині',
                'verbose_name_plural': 'Товари в корзині',
            },
        ),
    ]
