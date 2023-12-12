from django import forms
from .models import BlogPost, Comment
from markdownx.fields import MarkdownxFormField


class BlogPostForm(forms.ModelForm):

    content = forms.CharField()
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    text = MarkdownxFormField()
    class Meta:
        model = Comment
        fields = ['text']
