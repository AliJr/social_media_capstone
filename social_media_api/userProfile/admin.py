from django.contrib import admin
from .models import Follow, Like, Notification


class LikeAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('user', 'like_type', 'post', 'comment', 'created_at')
    
    # Enable sorting by these fields in the admin
    ordering = ('-created_at',)  # Sort by created_at in descending order
    
    # Optional: Adding filters in the admin sidebar
    list_filter = ('like_type', 'user', 'created_at')
    
    # Optional: Add search functionality in the admin
    search_fields = ('user__username', 'like_type', 'post__title', 'comment__content')


class FollowAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('follower', 'following', 'created_at')
    
    # Enable sorting by these fields in the admin
    ordering = ('-created_at',)  # Sort by created_at in descending order
    
    # Optional: Adding filters in the admin sidebar
    list_filter = ('follower', 'following', 'created_at')
    
    # Optional: Add search functionality in the admin
    search_fields = ('follower__username', 'following__username')


class NotificationAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('user', 'notification_type', 'created_at', 'is_read')
    
    # Enable sorting by these fields in the admin
    ordering = ('-created_at',)  # Sort by created_at in descending order
    
    # Optional: Adding filters in the admin sidebar
    list_filter = ('notification_type', 'user', 'is_read', 'created_at')
    
    # Optional: Add search functionality in the admin
    search_fields = ('user__username', 'notification_type')

# Register the Notification model with the NotificationAdmin configuration
admin.site.register(Notification, NotificationAdmin)

# Register the Follow model with the FollowAdmin configuration
admin.site.register(Follow, FollowAdmin)
# Register the Like model with the LikeAdmin configuration
admin.site.register(Like, LikeAdmin)
