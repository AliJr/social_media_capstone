# **1. Models and Serializers**
import re
from django.contrib.auth import get_user_model
from posts.models import Post, Comment
from userProfile.models import Like, Follow, Notification
from rest_framework import serializers

# **2. Tokens and password hasshing**
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


# user serializer class that handles all CRUD operations
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,  # Password is write-only to prevent it from being included in the response
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        # Create a new user using the validated data
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=make_password(
                validated_data["password"],
            ),
        )
        # Create a token for the new user
        token = Token.objects.create(user=user)

        # Return the user along with the token
        return user, token

    def update(self, user, validated_data):
        # Check if password is provided in the update request
        password = validated_data.get("password", None)
        # If password is provided, hash it before saving
        if password:
            # Manually hash the password using make_password
            validated_data["password"] = make_password(password)
        # Pass the updated validated data to the parent class to update other fields
        user = super().update(user, validated_data)
        # If the password was updated, save the request
        user.save()
        return user


# post serializer class that handles all CRUD operations
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author", "created_at"]


# Comment Serializer class that handle all CRUD operations
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author", "created_at"]

    # overriding update to remove post from validated data before saving
    def update(self, instance, validated_data):
        validated_data.pop("post", None)
        return super().update(instance, validated_data)


# Like Serializer class that handle all CRUD operations
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
        read_only_fields = ["user", "created_at"]
        

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'following', 'created_at']
        read_only_fields = ['follower','created_at']
        
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'notification_type', 'created_at', 'is_read', 'like', 'follow', 'comment']

    # Optionally, we can add more custom fields or methods to format related data
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Add related object details like the user who created the like, follow, or comment
        if instance.like:
            representation['like_details'] = {
                'post': instance.like.post.title if instance.like.post else None,
                'comment': instance.like.comment.content if instance.like.comment else None,
                'user': instance.like.user.username,
            }
        elif instance.follow:
            representation['follow_details'] = {
                'follower': instance.follow.followers.username,
                'followee': instance.follow.followees.username,
            }
        elif instance.comment:
            representation['comment_details'] = {
                'post': instance.comment.post.title,
                'author': instance.comment.author.username,
                'content': instance.comment.content,
            }
        return representation