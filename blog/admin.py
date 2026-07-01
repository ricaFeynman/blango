from django.contrib import admin
from .models import Tag, Post, Comment

class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('slug', 'published_at')

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, AdminPost)
admin.site.register(Comment)
