from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
