"""Модуль содержит пользовательские разрешения для работы с объектами API."""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешает доступ на чтение всем пользователям.

    Изменение объекта разрешается только его владельцу.
    """

    def has_object_permission(self, request, view, obj):
        """Проверяет разрешение на доступ к объекту."""
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
