from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Product


class ProductsPageTest(TestCase):
    def test_check_content_is_correct(self):
        products_page = self.client.get('/products/')
        self.assertTemplateUsed(products_page, "products/products.html")
        products_page_template_output = render_to_response("products/products.html",{'products': Product.objects.all()}).content
        self.assertEquals(products_page.content, products_page_template_output)