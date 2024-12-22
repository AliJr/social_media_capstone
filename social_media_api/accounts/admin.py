# **1. Admin and Models**
from django.contrib import admin  
from .models import User, Follow, Like  



admin.site.register(User)
admin.site.register(Follow)
admin.site.register(Like)