from django.db import models

class Supplier(models.Model):
    """
    This model stores the information of the product suppliers
    """
    supplier_name = models.CharField(max_length=150)
    email = models.EmailField()
    description = models.TextField(default="No Description")
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __unicode__(self):
        return self.supplier_name


class Customer(models.Model):
    """
    This model stores the data for the customers.
    Not using Django defualt User model to keep things simple
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __unicode__(self):
        return self.first_name


class Category(models.Model):
    """
    The model to handle categorising the product
    """
    category_name = models.CharField(max_length=50)
    category_description = models.TextField(default="No Description")
    category_image = models.URLField(help_text='The link to the service where the category' 
        ' image is stored')

    def __unicode__(self):
        return self.category_name


class Product(models.Model):
    """         
    The model for handling information about the product
    """
    product_name = models.CharField(max_length=150, unique=True)
    product_desription = models.TextField(default="No Description")
    product_size = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier)
    category = models.ForeignKey(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_color = models.CharField(max_length=50)
    product_image = models.URLField(help_text='The link to the service where the product' 
        ' image is stored')
    product_quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True, help_text='The day the product was added')
    date_updated = models.DateTimeField(auto_now=True, help_text='The day the product was updated')

    def __unicode__(self):
        return self.product_name

class Order(models.Model):
    """
    The model to handle to orders for a products
    """
    customer = models.ForeignKey(Customer)
    product = models.ManyToManyField(Product)
    qunatity_ordered = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text='The total cost of'
        ' products ordered')
    date_order = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.total_cost




