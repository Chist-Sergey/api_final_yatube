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
    path('', APIPost.as_view(), name='posts'),
    path('posts/<int:post_id>/', APIPostDetail.as_view(), name='post_id'),
    path('posts/<int:post_id>/comments', APIComment.as_view(), name='comments'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', APICommentDetal.as_view(), name='comment'),
    path('group/', APIGroup.as_view(), name='group'),
    path('follow/', APIFollow.as_view(), name='follow')
]
