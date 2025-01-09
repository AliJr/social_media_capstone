# **1. Admin and Models**
from django.contrib import admin
from .models import Post, Comment



class PostAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'created_at', 'updated_at', 'image_url')
    
    # Enable sorting by these fields in the admin
    ordering = ('-created_at',)  # Sort by created_at in descending order
    
    # Optional: Adding filters in the admin sidebar
    list_filter = ('author', 'created_at')

    # Optional: Add search functionality in the admin
    search_fields = ('title', 'content')



class CommentAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('author', 'post', 'created_at', 'updated_at', 'content')
    
    # Enable sorting by these fields in the admin
    ordering = ('-created_at',)  # Sort by created_at in descending order
    
    # Optional: Adding filters in the admin sidebar
    list_filter = ('author', 'post', 'created_at')
    
    # Optional: Add search functionality in the admin
    search_fields = ('author__username', 'content', 'post__title')

# Register the Post model with the PostAdmin configuration
admin.site.register(Post, PostAdmin)

# Register the Comment model with the CommentAdmin configuration
admin.site.register(Comment, CommentAdmin)

