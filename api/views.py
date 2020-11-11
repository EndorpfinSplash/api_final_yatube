from rest_framework import viewsets, permissions, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
from .models import Post, Comment, Follow, Group, User


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user,
                        post_id=self.kwargs['post_id'])

    def get_queryset(self):
        return Comment.objects.all().filter(post_id=self.kwargs['post_id'])


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=following__username', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return Follow.objects.all() #.filter(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    # search_fields = ['=group_id__id']

    # def get_queryset(self):
    #     return Group.objects.all().filter(group_id=self.request.user)