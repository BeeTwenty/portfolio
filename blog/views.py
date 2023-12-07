from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
import markdown

def blog_index(request):
    posts = BlogPost.objects.order_by('-date_posted')
    for post in posts:
        post.content = markdown.markdown(post.content)  # Convert Markdown to HTML
    return render(request, 'blog_index.html', {'posts': posts})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

