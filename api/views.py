from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Follow, Group, Post, User
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer)
PERMISSION_CLASSES = [IsAuthenticatedOrReadOnly]


class ListCreateOnlyModelViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = PERMISSION_CLASSES
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = PERMISSION_CLASSES

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        params = {
            'post_id': self.kwargs.get('post_id'),
            'author': self.request.user,
        }
        serializer.save(**params)


class FollowViewSet(ListCreateOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = ['following', ]
    search_fields = ['user__username', 'following__username', ]

    def get_queryset(self):
        following = get_object_or_404(User, username=self.request.user)
        return Follow.objects.filter(following=following)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(ListCreateOnlyModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = GroupSerializer
