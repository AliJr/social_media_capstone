# **1. Token and Permissions**
from .permissions import UserPermission, PostPermission
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action

# **2. Models and Serializers**
from .serializers import (
    UserSerializer,
    PostSerializer,
    CommentSerializer,
    LikeSerializer,
    FollowSerializer
)
from django.contrib.auth import get_user_model
from posts.models import Post, Comment
from accounts.models import Like, Follow
from rest_framework.serializers import ValidationError

# **3. ViewSets, views and mixins**
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)

# **4. Response Handling**
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
    filterset_fields = ["username", "email"]
    search_fields = ["username", "email"]
    ordering_fields = ["username", "email", "date_joined"]

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
                    "email": user.email,
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
    filterset_fields = ["author", "title", "content"]
    search_fields = ["title", "content"]
    ordering_fields = ["title", "created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Comment ViewSet
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [PostPermission]
    filterset_fields = ["author", "post", "content"]
    search_fields = ["content"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        # Set the author to the current user when creating a comment
        serializer.save(author=self.request.user)


# Like ViewSet
class LikeViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
):
    serializer_class = LikeSerializer

    def get_queryset(self):
        if self.request.user.is_staff:  # Check if the user is an admin
            return Like.objects.all()  # Admin can see all likes
        return Like.objects.filter(
            user=self.request.user
        )  # Regular users can only see their own likes

    def perform_create(self, serializer):
        like_type = self.request.data.get("like_type")
        post_id = self.request.data.get("post")
        comment_id = self.request.data.get("comment")
        # Check that the user is not liking both a post and a comment at the same time
        if like_type == "post":
            if not post_id:
                raise ValidationError("Post ID is required for liking a post.")
            if comment_id != "":
                raise ValidationError(
                    "You cannot like both a post and a comment in the same request."
                )
            # Ensure the user has not already liked this post
            if Like.objects.filter(user=self.request.user, post=post_id).exists():
                raise ValidationError("You have already liked this post.")

        elif like_type == "comment":
            if not comment_id:
                raise ValidationError("Comment ID is required for liking a comment.")
            if post_id != "":
                raise ValidationError(
                    "You cannot like both a post and a comment in the same request."
                )
            # Ensure the user has not already liked this comment
            if Like.objects.filter(user=self.request.user, comment=comment_id).exists():
                raise ValidationError("You have already liked this comment.")

        # If everything is valid, create the like
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """
        Override the default destroy method to add custom behavior
        for deleting likes.
        """
        try:
            # Retrieve the like object
            like = self.get_object()

            # If the user is not an admin, ensure they can only delete their own likes
            if not request.user.is_staff and like.user != request.user:
                return Response(
                    {"error": "You can only delete your own likes."}, status=403
                )

            # Proceed with deletion
            like.delete()

            return Response({"message": "Like deleted successfully"}, status=204)
        except Like.DoesNotExist:
            return Response({"error": "Like not found."}, status=404)

    # Override the list method to allow fetching the likes
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of likes for the current user.
        Optionally filter by like_type (post or comment).
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FollowViewSet(ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer