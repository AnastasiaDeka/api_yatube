"""
Конфигурация приложения posts.

Определяет настройки приложения для управления постами.
"""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Класс конфигурации приложения posts."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
