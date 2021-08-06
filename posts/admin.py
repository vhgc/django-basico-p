""" Post admin classes"""
# Django
from django.contrib import admin

from posts.models import Post
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts Admin model"""

    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_filter = (
                'created',
                'modified'
    )