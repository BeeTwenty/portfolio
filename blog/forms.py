from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    content = forms.CharField()
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

