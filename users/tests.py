import unittest
from django.test import TestCase
from rest_framework import status
from .models import User
from .serializers import UsersSerializer


class UserAPITestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            'email': 'test@user.com',
            'password': 'test'
        }

    def test_get_user_register(self) -> None:
        """Тестирование регистрации нового пользователя."""
        data = {
            'email': 'test@user.com',
            'password': 'test'
        }
        response = self.client.post(
            '/users/users/',
            data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestUsersSerializer(unittest.TestCase):
    def test_fields(self):
        serializer = UsersSerializer()
        self.assertEqual(serializer.Meta.model, User)
        self.assertEqual(serializer.Meta.fields, ['id', 'first_name', 'last_name', 'email', 'phone'])
