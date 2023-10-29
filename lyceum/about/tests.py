import django.test
from django.test import TestCase


# Create your tests here.
class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = django.test.Client().get('/about')
        self.assertEqual(response.status_code, 200)
