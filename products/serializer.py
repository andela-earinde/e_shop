from rest_framework import serializers
from products.models import (Product, Category,
    Order, Customer, Supplier)

class CategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = Category

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
    
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer