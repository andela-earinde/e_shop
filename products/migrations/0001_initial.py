# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
                ('category_description', models.TextField(default=b'No Description')),
                ('category_image', models.URLField(help_text=b'The link to the service where the categoryimage is stored')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qunatity_ordered', models.IntegerField(default=0)),
                ('total_cost', models.DecimalField(help_text=b'The total cost ofproducts ordered', max_digits=10, decimal_places=10)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to='products.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(unique=True, max_length=150)),
                ('product_desription', models.TextField(default=b'No Description')),
                ('product_size', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=10, decimal_places=10)),
                ('product_color', models.CharField(max_length=50)),
                ('product_image', models.URLField(help_text=b'The link to the service where the productimage is stored')),
                ('product_quantity', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(help_text=b'The day the product was added', auto_now_add=True)),
                ('date_updated', models.DateTimeField(help_text=b'The day the product was updated', auto_now=True)),
                ('category', models.ForeignKey(to='products.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('supplier_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=75)),
                ('description', models.TextField(default=b'No Description')),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(to='products.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
            preserve_default=True,
        ),
    ]
