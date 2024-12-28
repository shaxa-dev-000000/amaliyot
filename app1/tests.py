from django.test import TestCase

# Create your tests here.
class TestApp1(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_base_page(self):
        response = self.client.get('/base/')
        self.assertEqual(response.status_code, 200)