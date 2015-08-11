# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, upload_to='categories', null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('symbol', models.CharField(max_length=16)),
                ('factor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.DecimalField(default=0.0, decimal_places=2, blank=True, null=True, max_digits=10)),
                ('name', models.CharField(max_length=128)),
                ('descripion', models.TextField(blank=True, null=True)),
                ('weight', models.DecimalField(default=None, blank=True, null=True, verbose_name='Weight (kg)', max_digits=10, decimal_places=8)),
                ('width', models.DecimalField(default=None, blank=True, null=True, verbose_name='Width (m)', max_digits=10, decimal_places=8)),
                ('height', models.DecimalField(default=None, blank=True, null=True, verbose_name='Height (m)', max_digits=10, decimal_places=8)),
                ('depth', models.DecimalField(default=None, blank=True, null=True, verbose_name='Depth (m)', max_digits=10, decimal_places=8)),
                ('categories', models.ManyToManyField(to='shop.Category')),
                ('currency', models.ForeignKey(blank=True, null=True, to='shop.Currency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('file', models.FileField(blank=True, upload_to='products', null=True)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('main_image', models.BooleanField(default=False)),
                ('item', models.ForeignKey(to='shop.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('net_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total net price')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total price')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('item', models.ForeignKey(to='shop.Item')),
                ('order', models.ForeignKey(to='shop.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=64, choices=[(0, 'Awaiting payment'), (1, 'Payed'), (2, 'Sent')])),
                ('order', models.ForeignKey(to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.DecimalField(default=0.0, decimal_places=2, blank=True, null=True, max_digits=10)),
                ('name', models.CharField(max_length=128, verbose_name='Payment name')),
                ('config', models.CharField(max_length=256, verbose_name='Config file')),
                ('currency', models.ForeignKey(blank=True, null=True, to='shop.Currency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShipmentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('price', models.DecimalField(default=0.0, decimal_places=2, blank=True, null=True, max_digits=10)),
                ('name', models.CharField(max_length=128)),
                ('enabled', models.BooleanField(default=True)),
                ('currency', models.ForeignKey(blank=True, null=True, to='shop.Currency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='shipmentmethod',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, to='shop.Tax'),
        ),
        migrations.AddField(
            model_name='paymentmethod',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, to='shop.Tax'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(to='shop.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ForeignKey(to='shop.ShipmentMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, to='shop.Tax'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(to='shop.Item'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
