# **1. Routers and Views**
from rest_framework.routers import DefaultRouter  
from .views import UserViewSet, PostViewSet, CommentViewSet, LikeViewSet, FollowViewSet, NotificationViewSet  
# **2. URLs**
from django.urls import path, include  



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'follow', FollowViewSet)
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [path('', include(router.urls)), ]