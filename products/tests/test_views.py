from django.core.urlresolvers import reverse
from products.views import (ProductView, CategoryView, SupplierView, 
    OrderView)
from products.models import (Product, Supplier, Customer,
    Category, Order)
from rest_framework import status
from rest_framework.test import APITestCase

class ProductsTestCase(APITestCase):
    product_category = ""
    product_supplier = ""

    def setUp(self):
        self.product_category = Category.objects.create(category_name="headsets", 
            category_description="very cool headsets", category_image="http:/amazon.com/beats.jpg")

        self.product_supplier = Supplier.objects.create(supplier_name="Apple", email="apple@apple.com", 
            description="cool company", phone="323232323", address="likin park", city="new brew", 
            state="old brew", country="USA")

        Product.objects.create(product_name="beats by dre",product_desription="cool headset",
            product_size="2l", category=self.product_category, price=200.00, product_color="red",
            product_image="http://amazon.com/beats_dre.jpg", product_quantity=20,
            supplier=self.product_supplier, is_available=True)

    #Test cases for GET /products/
    def test_retrieve_all_products_when_the_product_route_is_requested(self):
        response = self.client.get('/products/')
        self.assertEqual(len(response.data), 1)

    def test_that_a_retrieved_product_contain_some_expected_data(self):
        response = self.client.get('/products/')
        data = dict(response.data[0])
        self.assertDictContainsSubset({"product_name": "beats by dre", "product_desription": "cool headset",
            "product_size":"2l", "price": "200.00", "product_color": "red",
             "product_image": "http://amazon.com/beats_dre.jpg", "product_quantity": 20,
             "is_available": True}, data)

    #test cases for POST /products/
    def test_that_a_new_product_is_saved_in_the_database_when_a_post_request_is_made(self):

        response = self.client.post('/products/', {"product_name": "iphone6", "product_desription": "nice phone",
            "product_size":"34", "price": "600.00", "product_color": "white",             
            "product_image": "http://amazon.com/iphone.jpg", "product_quantity": 20,
            "is_available": True, "supplier": "http://testserver/supplier/1/", 
            "category": "http://testserver/categories/1/"})

        self.assertDictContainsSubset({"product_name": "iphone6", "product_desription": "nice phone",
            "product_size":"34", "price": "600.00", "product_color": "white",             
            "product_image": "http://amazon.com/iphone.jpg", "product_quantity": 20,
            "is_available": True}, response.data)

    def test_that_an_error_is_returned_if_the_required_fields_are_not_set_when_posting(self):
        response = self.client.post('/products/',{})

        self.assertDictContainsSubset({'product_name': ['This field is required.'],
            'category': ['This field is required.'], 'price': [u'This field is required.']}, response.data)

    #test cases for GET /products/{pk}
    def test_a_product_is_retrieved_when_its_primary_key_sent_is_with_a_get_request(self):
        response = self.client.get('/products/1/')

        self.assertDictContainsSubset({"product_name": "beats by dre", "product_desription": "cool headset",
            "product_size":"2l", "price": "200.00", "product_color": "red",
             "product_image": "http://amazon.com/beats_dre.jpg", "product_quantity": 20,
             "is_available": True}, response.data)

    def test_that_a_not_found_response_is_sent_if_a_wrong_primary_key_is_sent_with_a_get_request(self):
        response = self.client.get('/products/10/')
        self.assertEqual({"detail": "Not found."}, response.data)
    
    #test cases for PUT /products/{pk}
    def test_a_product_is_updated_when_a_put_request_is_made_with_a_primary_key_and_the_updated_data(self):
        response = self.client.put('/products/1/', {"product_name": "beats", "product_desription": "very cool headset",
            "product_size":"2l", "price": "200.00", "product_color": "red",
             "product_image": "http://amazon.com/beats_dre.jpg", "product_quantity": 20,
             "is_available": True, "supplier":"http://testserver/supplier/1/",
             "category": "http://testserver/categories/1/"})

        self.assertDictContainsSubset({"product_name": "beats", "product_desription": "very cool headset",
            "product_size":"2l", "price": "200.00", "product_color": "red",
             "product_image": "http://amazon.com/beats_dre.jpg", "product_quantity": 20,
             "is_available": True}, response.data);

    def test_a_product_is_not_updated_when_a_put_request_is_made_and_the_data_is_incomplete(self):
        response = self.client.put('/products/1/', {"product_name": "", "product_desription": "very cool headset",
            "product_size":"2l", "price": "200.00", "product_color": "red",
             "product_image": "http://amazon.com/beats_dre.jpg", "product_quantity": 20,
             "is_available": True, "supplier":"http://testserver/supplier/1/",
             "category": "http://testserver/categories/1/"})

        self.assertEqual({"product_name": ["This field may not be blank."]}, response.data)

    #test case for DELETE /products/{pk}
    def test_a_product_is_deleted_when_a_delete_request_is_made_with_the_products_primary_key(self):
        response = self.client.delete('/products/1/')

        self.assertEqual(response.data, None)

    def test_a_not_found_error_is_returned_if_a_delete_request_is_made_with_an_invalid_pk(self):
        response = self.client.delete('/products/3/')

        self.assertEqual({'detail': 'Not found.'},response.data)


class CategoryTestCase(APITestCase):
    product_category=""

    def setUp(self):
        self.product_category = Category.objects.create(category_name="headsets", 
            category_description="very cool headsets", category_image="http://amazon.com/beats.jpg")


    #test cases for GET /categries/
    def test_retrieves_all_the_category_when_a_get_request_is_made(self):
        response = self.client.get('/categories/')

        data = [{"id": 1, "category_name": "headsets", "category_description": "very cool headsets",
            "category_image": "http://amazon.com/beats.jpg"}]

        self.assertEqual(len(response.data), 1)   
        self.assertEqual(response.data, data)

    #test cases for POST /categories/
    def test_a_new_category_is_created_when_a_post_made_with_the_required_data(self):
        response = self.client.post("/categories/", {"category_name": "cups", 
            "category_description": "cool cups", "category_image": "http://samzon.com/cup.jpg"})

        data = {"id": 2, "category_name": "cups", "category_description": "cool cups",
            "category_image": "http://samzon.com/cup.jpg"}

        self.assertEqual(response.data, data)

    def test_a_category_is_not_created_when_some_the_required_fields_are_not_supplied(self):
        response = self.client.post("/categories/", {"category_name": "", 
            "category_description": "cool cups", "category_image": "http://samzon.com/cup.jpg"})

        data = {"category_name": ["This field may not be blank."]}

        self.assertEqual(response.data, data)

    #test cases for PUT /categories/{pk}
    def test_a_category_updated_when_put_request_is_made_with_the_pk(self):
        response = self.client.put("/categories/1/",{"category_name": "headphones", 
            "category_description": "very cool headphones","category_image": "http://amazon.com/beats.jpg"})

        data = {"id": 1, "category_name": "headphones", "category_description": "very cool headphones",
            "category_image": "http://amazon.com/beats.jpg"}

        self.assertEqual(response.data, data)

class OrderTestCase(APITestCase):
    ord_customers = ""
    ord_products = ""
    product_category = ""
    product_supplier = ""
    def setUp(self):
        self.product_category = Category.objects.create(category_name="headsets", 
            category_description="very cool headsets", category_image="http:/amazon.com/beats.jpg")

        self.product_supplier = Supplier.objects.create(supplier_name="Apple", email="apple@apple.com", 
            description="cool company", phone="323232323", address="likin park", city="new brew", 
            state="old brew", country="USA")
        self.ord_products = Product.objects.create(product_name="beats by dre",product_desription="cool headset",
            product_size="2l", category=self.product_category, price=200.00, product_color="red",
            product_image="http://amazon.com/beats_dre.jpg", product_quantity=20,
            supplier=self.product_supplier, is_available=True)
        self.ord_customers = Customer.objects.create(first_name="eniola", last_name="arinde",
            email="eniola@yahoo.com", phone="121212", address="new city", city="compton",
            state="new cost", country="south brigde")

        orders = Order(customer=self.ord_customers, qunatity_ordered=2, total_cost=400.00)
        orders.save()
        orders.product.add(self.ord_products)


    #test cases for GET /orders/
    def test_retrieves_all_orders_when_a_get_request_is_made(self):
        response = self.client.get('/orders/')

        data = dict(response.data[0])

        self.assertEqual(len(response.data), 1)
        self.assertDictContainsSubset({'customer':'http://testserver/customers/1/', 
            'product': ['http://testserver/products/1/'], 'qunatity_ordered': 2}, data)

    #test cases for POST /orders/
    def test_add_a_new_order_when_a_post_request_is_made(self):
        response = self.client.post('/orders/', {'customer': 'http://testserver/customers/1/', 
            'product': ['http://testserver/products/1/'], 'qunatity_ordered': 4, 'total_cost': 800.00})

        self.assertDictContainsSubset({'customer': 'http://testserver/customers/1/', 
            'product': ['http://testserver/products/1/'], 'qunatity_ordered': 4, 'total_cost': '800.00'},
            response.data)
