from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import CustomUser


class UserTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        url = reverse('register')
        data = {'username': 'testuser', 'password': 'testpassword', 'email': 'testuser@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())

    def test_login_user(self):
        user = CustomUser.objects.create_user(username='testuser',
                                              password='testpassword',
                                              email='testuser@example.com')
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
