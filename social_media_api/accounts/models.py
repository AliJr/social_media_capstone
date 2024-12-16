# **1. Models and Authentication**
from django.db import models  
from django.contrib.auth.models import AbstractUser  



# Custom user model extending the built in user model from Django
class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False) # mandatory field when creating user: (unique), cant be empty in forms or database
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="assets/profile_pictures/", blank=True, null=True
    )
    location = models.CharField(max_length=100, blank=True, null=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="follower", blank=True
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="following", blank=True
    )

    def __str__(self):
        return self.username

    # functions to count followers and followings
    def count_followers(self):
        return self.followers.count()
    def count_followings(self):
        return self.followings.count()

    # functions to check if user is following or followed
    def is_following(self, user):
        return self.followings.filter(pk=user.pk).exists()
    def is_follower(self, user):
        return self.followers.filter(pk=user.pk).exists()
    
    # functions to get followers and followings
    def get_followings(self):
        return self.followings.all()
    def get_followers(self):
        return self.followers.all()