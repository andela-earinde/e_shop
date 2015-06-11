from products.models import (Product, Category,
    Order, Customer, Supplier)
from products.serializer import (ProductSerializer, CategorySerializer, 
    SupplierSerializer, OrderSerializer, CustomerSerializer)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class ProductView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing products instances.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CategoryView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class SupplierView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing supplies instances.
    """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

class OrderView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing supplies instances.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CustomerView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing supplies instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

