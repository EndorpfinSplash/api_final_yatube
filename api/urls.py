from django.urls import path, include

# from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('group', GroupViewSet, basename='group_basename')
router.register('follow', FollowViewSet, basename='follow_basename')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment_basename')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns += [
#     path('api-token-auth/', views.obtain_auth_token)
# ]
