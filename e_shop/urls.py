from django.conf.urls import patterns, include, url
from django.contrib import admin
from products.views import (ProductView, CategoryView, 
    SupplierView, OrderView, CustomerView)
from rest_framework.routers import DefaultRouter

#register the url routes here
router = DefaultRouter()
router.register(r'products', ProductView)
router.register(r'categories', CategoryView)
router.register(r'supplier', SupplierView)
router.register(r'orders', OrderView)
router.register(r'customers', CustomerView)

urlpatterns = patterns('',
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
