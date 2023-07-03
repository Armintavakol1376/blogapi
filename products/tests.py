from django.test import TestCase
from django.urls import reverse
from .models import Products


class ProductsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.products = Products.objects.create(
            name="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            price="1234567890123",
)

    def test_products_content(self):
        self.assertEqual(self.products.name, "A good title")
        self.assertEqual(self.products.subtitle, "An excellent subtitle")
        self.assertEqual(self.products.author, "Tom Christie")
        self.assertEqual(self.products.price, "1234567890123")

    def test_products_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "products/products_list.html")


