# **1. Models and User Authentication model**
from django.db import models
from posts.models import Post, Comment
from django.contrib.auth import get_user_model
# Create your models here.

# Like class with author, post and comment as foreign keys
class Like(models.Model):
    # Define the choices for the like type
    LIKE_CHOICES = (
        ("post", "Post"),
        ("comment", "Comment"),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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
    followers = models.ForeignKey(get_user_model(),related_name='follower', on_delete=models.CASCADE, db_index=True) #The user who is following
    followees = models.ForeignKey(get_user_model(),related_name='followee', on_delete=models.CASCADE, db_index=True) #The user being followed.
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Ensure the follower-followee pair is unique
        unique_together = ('followers', 'followees')
        
        ordering = ["-created_at"]
        
    def __str__(self):
        return f"{self.followers.username} follows {self.followees.username}"
    
    
from django.db import models
from django.contrib.auth import get_user_model

# Notification model to track likes, follows, and comments
class Notification(models.Model):
    NOTIFICATION_CHOICES = (
        ('like', 'Like'),
        ('follow', 'Follow'),
        ('comment', 'Comment'),
    )
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    # Related object for notification context
    like = models.ForeignKey(Like, null=True, blank=True, on_delete=models.CASCADE)
    follow = models.ForeignKey(Follow, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} has a new {self.notification_type} notification"
    
    class Meta:
        ordering = ['-created_at']
