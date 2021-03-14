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
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/posts/', APIPost.as_view(), name='posts'),
    path('api/v1/posts/<int:post_id>/', APIPostDetail.as_view(), name='post_id'),
    path('api/v1/posts/<int:post_id>/comments/', APIComment.as_view(), name='comments'),
    path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/', APICommentDetal.as_view(), name='comment'),
    path('api/v1/group/', APIGroup.as_view(), name='group'),
    path('api/v1/follow/', APIFollow.as_view(), name='follow')
]
