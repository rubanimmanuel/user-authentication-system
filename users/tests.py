from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserRegistrationTest(APITestCase):
    def test_registration(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "StrongPass123!",
            "password2": "StrongPass123!",
        }
        response = self.client.post(reverse('auth_register'), data)
        self.assertEqual(response.status_code, 201)