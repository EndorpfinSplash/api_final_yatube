from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('group', GroupViewSet, basename='group_basename')
router.register('follow', FollowViewSet, basename='follow_basename')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment_basename')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
