# **1. Models and Serializers**
from django.contrib.auth import get_user_model
from rest_framework import serializers

# **2. Tokens and password hasshing**
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


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
        password = validated_data.get('password', None)
        # If password is provided, hash it before saving
        if password:
            # Manually hash the password using make_password
            validated_data['password'] = make_password(password)
        # Pass the updated validated data to the parent class to update other fields
        instance = super().update(user, validated_data)
        # If the password was updated, save the request
        user.save()
        return instance