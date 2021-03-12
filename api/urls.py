from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path

from .views import (
    APIPost, 
    APIPostDetail, 
    APIComment, 
    APICommentDetal,
    APIFollow,
    APIGroup,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', APIPost, name='posts'),
    path('posts/<int:post_id>/', APIPostDetail, name='post_id'),
    path('posts/<int:post_id>/comments', APIComment, name='comments'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', APICommentDetal, name='comment'),
    path('group/', APIGroup, name='group'),
    path('follow/', APIFollow, name='follow')
]
