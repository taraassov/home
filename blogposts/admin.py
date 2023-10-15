from django.contrib import admin

from blogposts.models import Blogpost


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview', 'created_at', 'is_published', 'views_count')
