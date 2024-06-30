import unittest
from django.urls import reverse
from .models import Module, Lesson
from .serializers import ModuleSerializer, LessonSerializer
from users.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class ModuleAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.user.set_password('test')
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)
        self.module = Module.objects.create(
            title='модуль 1',
            description='описание',
            owner=self.user,
            )

    def test_get_module_create(self):
        """
        Тестирование создания модуля
        """
        data = {
            'title': 'модуль 1',
            'description': 'описание',
            'owner': self.user
        }

        response = self.client.post(
            reverse('module:module-create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_get_module_list(self):
        """
        Тестирование получения списка модулей
        """
        response = self.client.get(
            reverse('module:module-list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_module_retrieve(self):
        """
        Тестирование просмотра отдельного модуля
        """
        response = self.client.get(
            reverse('module:module-get', kwargs={'pk': self.module.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_module_update(self):
        """
        Тестирование редактирования модуля
        """
        data = {
            'title': 'модуль 2',
            'description': 'описание новое',
            'owner': self.user
        }

        response = self.client.patch(
            reverse('module:module-update', kwargs={'pk': self.module.pk}),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_module_delete(self):
        """
        Тестирование удаления модуля
        """
        response = self.client.delete(
            reverse('module:module-delete', kwargs={'pk': self.module.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )


class LessonAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru')
        self.user.set_password('test')
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)
        self.lesson = Lesson.objects.create(
            title='урок 1',
            body='содержание урока 1',
            owner=self.user,
            )

    def test_get_lesson_create(self):
        """
        Тестирование создания урока
        """
        data = {
            'title': 'урок 1',
            'body': 'содержание урока 1',
            'owner': self.user
        }

        response = self.client.post(
            reverse('module:lesson-create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_get_lesson_list(self):
        """
        Тестирование получения списка уроков
        """
        response = self.client.get(
            reverse('module:lesson-list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lesson_retrieve(self):
        """
        Тестирование просмотра отдельного урока
        """
        response = self.client.get(
            reverse('module:lesson-get', kwargs={'pk': self.lesson.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lesson_update(self):
        """
        Тестирование редактирования урока
        """
        data = {
            'title': 'урок 1',
            'body': 'содержание урока 1',
            'owner': self.user
        }

        response = self.client.patch(
            reverse('module:lesson-update', kwargs={'pk': self.lesson.pk}),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_get_lesson_delete(self):
        """
        Тестирование удаления урока
        """
        response = self.client.delete(
            reverse('module:lesson-delete', kwargs={'pk': self.lesson.pk}),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )


class ModuleSerializerTestCase(unittest.TestCase):
    def test_module_serializer_fields(self):
        serializer = ModuleSerializer()
        self.assertEqual(serializer.Meta.model, Module)
        self.assertEqual(serializer.Meta.fields, ('pk', 'title', 'description', 'owner'))
        self.assertEqual(serializer.Meta.read_only_fields, ('owner',))


class LessonSerializerTestCase(unittest.TestCase):
    def test_lesson_serializer_fields(self):
        serializer = LessonSerializer()
        self.assertEqual(serializer.Meta.model, Lesson)
        self.assertEqual(serializer.Meta.fields, ('pk', 'title', 'body', 'video_url', 'module', 'owner'))
        self.assertEqual(serializer.Meta.read_only_fields, ('owner',))
