from django import forms
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):

    content = forms.CharField()
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
