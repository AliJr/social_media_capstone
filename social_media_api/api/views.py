# **1. Token and Permissions**
from .permissions import UserPermission, PostPermission 
from rest_framework.authtoken.models import Token  
# **2. Models and Serializers**
from .serializers import UserSerializer, PostSerializer  
from django.contrib.auth import get_user_model  
from posts.models import Post
# **3. ViewSets**
from rest_framework.viewsets import ModelViewSet  
# **4. Response Handling**
from rest_framework.response import Response  
from rest_framework import status  

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    filterset_fields = ['username', 'email']
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'email', 'date_joined']
    
    def create(self, request, *args, **kwargs):
        # Validate and save the user using the serializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()  # Get both user and token
            # Send back user details and token in the response
            return Response(
                {
                    "id": user.id,
                    "username": user.username,
                    'email': user.email,
                    "token": token.key,  # Return the token
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [PostPermission]
    filterset_fields = ['author', 'title', 'content']
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at', 'updated_at']
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)