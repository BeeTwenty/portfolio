from django import forms
from .models import BlogPost
from markdownx.fields import MarkdownxFormField

class BlogPostForm(forms.ModelForm):

    content = MarkdownxFormField()
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

