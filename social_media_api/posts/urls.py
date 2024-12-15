from django.urls import path
from .views import PostListView, PostDetailView, UserRegistrationView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
