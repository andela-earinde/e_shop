from products.models import (Product, Category,
    Order, Customer, Supplier)
from products.serializer import (ProductSerializer, CategorySerializer, 
    SupplierSerializer, OrderSerializer, CustomerSerializer)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters

class ProductView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing products instances.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("product_name", "product_desription")

class CategoryView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("category_name", "category_description")

class SupplierView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing supplies instances.
    """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("supplier_name", "description")

class OrderView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order instances.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CustomerView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing customer instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ("first_name", "last_name")

