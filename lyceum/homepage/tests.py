import http

import django.test

class StaticURLTests(django.test.TestCase):
    def test_homepage_endpoint(self):
        response = django.test.Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint_status(self):
        response = django.test.Client().get('/coffee')
        self.assertEqual(response.status_code, http.HTTPStatus.IM_A_TEAPOT)

    def test_coffee_endpoint_text(self):
        response = django.test.Client().get('/coffee')
        self.assertEqual(response.content, 'Я чайник'.encode())