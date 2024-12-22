# **1. Models and Authentication**
from django.db import models  
from django.contrib.auth.models import AbstractUser  
from posts.models import Post, Comment



# Custom user model extending the built in user model from Django
class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False) # mandatory field when creating user: (unique), cant be empty in forms or database
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="assets/profile_pictures/", blank=True, null=True
    )
    location = models.CharField(max_length=100, blank=True, null=True)
    #followers = models.ManyToManyField("self", symmetrical=False, related_name="follower", blank=True)
    #followings = models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)

    def __str__(self):
        return self.username

    # functions to count followers and followings
    #def count_followers(self):
    #   return self.followers.count()
    #def count_followings(self):
        #return self.followings.count()

    # functions to check if user is following or followed
    #def is_following(self, user):
        #return self.followings.filter(pk=user.pk).exists()
    #def is_follower(self, user):
        #return self.followers.filter(pk=user.pk).exists()
    
    # functions to get followers and followings
    #def get_followings(self):
        #return self.followings.all()
    #def get_followers(self):
        #return self.followers.all()
    
    
    
# Like class with author, post and comment as foreign keys
class Like(models.Model):
    # Define the choices for the like type
    LIKE_CHOICES = (
        ("post", "Post"),
        ("comment", "Comment"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    like_type = models.CharField(max_length=10, choices=LIKE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ensure that a user can only like a post once
        unique_together = ["user", "post", "comment"]

    def __str__(self):
        return f"Like by {self.user.username} on {self.like_type} {self.post or self.comment}"

# Follow model to link build following system
class Follow(models.Model):
    followers = models.ForeignKey(User,related_name='follower', on_delete=models.CASCADE, db_index=True) #The user who is following
    followees = models.ForeignKey(User,related_name='followee', on_delete=models.CASCADE, db_index=True) #The user being followed.
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Ensure the follower-followee pair is unique
        unique_together = ('followers', 'followees')
        
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"{self.followers.username} follows {self.followees.username}"