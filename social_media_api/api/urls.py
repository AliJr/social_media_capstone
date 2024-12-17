# **1. Routers and Views**
from rest_framework.routers import DefaultRouter  
from .views import UserViewSet, PostViewSet, CommentViewSet, LikeViewSet  
# **2. URLs**
from django.urls import path, include  



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [path('', include(router.urls)), ]