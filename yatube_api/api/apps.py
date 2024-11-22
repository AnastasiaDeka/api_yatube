"""Конфигурация приложения API для управления REST API функционалом."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфигурация приложения API для управления REST API функционалом."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
