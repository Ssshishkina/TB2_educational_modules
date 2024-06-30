from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
      Проверка на наличие прав администратора
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsOwner(BasePermission):
    """
    Проверка на наличие прав владельца модуля
    """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
