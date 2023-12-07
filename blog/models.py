from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title