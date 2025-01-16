from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/index.html')


class ProductListViewTestCase(TestCase):
    fixtures = ['products.json', 'categories.json']

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Product.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(response.context_data['object_list']), list(products[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        products = Product.objects.filter(category=category)

        path = reverse('products:category', kwargs={'cat_id': category.id})
        response = self.client.get(path)
        self.assertEqual(list(response.context_data['object_list']), list(products[:3]))




