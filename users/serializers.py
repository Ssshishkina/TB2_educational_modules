from rest_framework import serializers
from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone']
