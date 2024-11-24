"""Сериализаторы для моделей Post, Group и Comment."""

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        """Мета-класс для настройки полей сериализатора."""

        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Мета-класс для настройки полей сериализатора."""

        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        """Мета-класс для настройки полей сериализатора."""

        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
        read_only_fields = ('post',)
