"""
Модуль для работы с API постов, групп и комментариев.

Содержит ViewSet'ы для работы с данными через Django Rest Framework.
"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.exceptions import PermissionDenied

from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Post, Group, Comment
from .permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
    """
    ViewSet для работы с постами.

    Только авторизованные пользователи могут создавать, редактировать
    и удалять посты.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Устанавливает автора поста как текущего пользователя."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Проверяет, что пользователь редактирует свой пост."""
        if self.get_object().author != self.request.user:
            raise PermissionDenied('Вы не можете редактировать чужой пост.')
        serializer.save()

    def perform_destroy(self, instance):
        """Проверяет, что пользователь удаляет свой пост."""
        if instance.author != self.request.user:
            raise PermissionDenied('Вы не можете удалить чужой пост.')
        instance.delete()


class GroupViewSet(ReadOnlyModelViewSet):
    """
    ViewSet для работы с группами.

    Пользователи могут просматривать список групп, но не могут их изменять.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    """
    ViewSet для работы с комментариями.

    Только авторизованные пользователи могут добавлять комментарии,
    редактировать и удалять их.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """Получает комментарии только для указанного поста."""
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        """Устанавливает автора комментария и привязывает его к посту."""
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)
