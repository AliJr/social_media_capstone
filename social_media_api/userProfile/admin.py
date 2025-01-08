from django.contrib import admin
from .models import Follow, Like, Notification

#Register your models here.
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Notification)