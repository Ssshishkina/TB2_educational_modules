from rest_framework import serializers
from modules.models import Module, Lesson


class ModuleSerializer(serializers.ModelSerializer):
    """Сериализатор модуля"""
    class Meta:
        model = Module
        fields = ('pk', 'title', 'description', 'owner')
        read_only_fields = ('owner',)


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор урока"""
    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'body', 'video_url', 'module', 'owner')
        read_only_fields = ('owner',)
