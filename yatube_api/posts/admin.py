"""
Модуль для регистрации моделей в админ-панели Django.

Позволяет управлять постами, группами и комментариями
через интерфейс администратора.
"""

from django.contrib import admin

from .models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    """
    Конфигурация отображения модели Post в админ-панели.

    Добавляет отображение полей, поиск и фильтры.
    """

    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
