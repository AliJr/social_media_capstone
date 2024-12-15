from django.db import models

# Post model with custom user as a foreign key
class Post(models.Model):
    author = models.ForeignKey('accounts.User', related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at}"