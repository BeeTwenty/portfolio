from django.contrib import admin
from .models import BlogPost, Comment, Like
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register(BlogPost, MarkdownxModelAdmin)
admin.site.register(Comment, MarkdownxModelAdmin)
admin.site.register(Like)


