# **1. Routers and Views**
from rest_framework.routers import DefaultRouter  
from .views import UserViewSet, PostViewSet  
# **2. URLs**
from django.urls import path, include  



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
