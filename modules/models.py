from django.db import models
from config import settings
from users.models import NULLABLE


class Module(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец модуля',
                              **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'модуль'
        verbose_name_plural = 'модули'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название урока')
    body = models.TextField(verbose_name='содержание урока')
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, **NULLABLE, verbose_name='модуль')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец урока',
                              **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
