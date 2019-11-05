from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductTests(TestCase):
    """Define the tests that run against Product models"""

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')


class ProductsPageTest(TestCase):

    def test_products_page_status_code_and_path(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_page_url_name(self):
        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)
