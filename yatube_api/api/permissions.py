"""Модуль содержит пользовательские разрешения для работы с объектами API."""

from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsAuthenticatedAndOwnerOrReadOnly(IsAuthenticated):
    """
    Разрешает доступ на чтение всем пользователям.

    Изменение объекта разрешается только его владельцу.
    """

    def has_object_permission(self, request, view, obj):
        """Проверяет разрешение на уровне объекта."""
        return request.method in SAFE_METHODS or obj.author == request.user
