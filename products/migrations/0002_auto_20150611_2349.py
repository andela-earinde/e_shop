# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.URLField(help_text=b'The link to the service where the category image is stored'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(help_text=b'The total cost of products ordered', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.URLField(help_text=b'The link to the service where the product image is stored'),
        ),
    ]
