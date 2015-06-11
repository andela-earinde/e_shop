from django.conf.urls import patterns, include, url
from django.contrib import admin
from products.views import Products

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'e_shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^products/$', Products.as_view(), name="products"),
    url(r'^admin/', include(admin.site.urls)),
)
