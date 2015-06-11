from django.contrib import admin
from products.models import (Product, Category,
    Order, Customer, Supplier)


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Supplier)



