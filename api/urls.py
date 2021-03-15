from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('group', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')
urlpatterns = [
    path('v1/', include(router.urls)),
]