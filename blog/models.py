from django.db import models
from django.utils import timezone
from django.conf import settings
from markdownx.models import MarkdownxField


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    date_posted = models.DateTimeField(default=timezone.now)


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = MarkdownxField()
    created_date = models.DateTimeField(default=timezone.now)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('post', 'user')
