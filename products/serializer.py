from rest_framework import serializers
from products.models import (Product, Category,
    Order, Customer)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product