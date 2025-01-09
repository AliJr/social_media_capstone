# **1. Admin and Models**
from django.contrib import admin  
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    # Define the fields to be displayed in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'bio', 'location', 'is_active', 'is_staff')
    
    # Add filters for email, location, and is_active
    list_filter = ('is_active', 'is_staff', 'location')
    
    # Define how to order the list of users
    ordering = ('username',)  # You can adjust this as needed (e.g., ordering by email or date joined)
    
    # Add search capability (optional)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'bio')
    
    # Customize the fields for the user edit page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_picture', 'location')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'bio', 'location', 'is_active', 'is_staff'),
        }),
    )
    
    # Define the filtering for the related fields (Optional)
    filter_horizontal = ('groups', 'user_permissions')

# Register the custom UserAdmin
admin.site.register(User, UserAdmin)