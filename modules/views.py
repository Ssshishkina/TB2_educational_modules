from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from modules.models import Module, Lesson
from modules.paginators import ModulePaginator, LessonPaginator
from modules.permissions import IsOwner
from modules.serializers import ModuleSerializer, LessonSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания модуля
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_module = serializer.save()
        new_module.owner = self.request.user
        new_module.save()


class ModuleListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка модулей
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ModulePaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра модуля
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class ModuleUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер обновления модуля
    """
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class ModuleDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления модуля
    """
    queryset = Module.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Контроллер создания урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """
    Контроллер просмотра списка уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер просмотра урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер обновления урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер удаления урока
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
