from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogPost, Comment, Like
from .forms import BlogPostForm, CommentForm
import markdown


def blog_index(request):
    posts = BlogPost.objects.order_by('-date_posted')
    
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


def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    likes = post.likes.all()
    is_liked = False
    if request.user.is_authenticated:
        is_liked = post.likes.filter(user=request.user).exists()

    comment_form = CommentForm() 
    if request.method == 'POST':
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user
                new_comment.save()
                return redirect('blog_post_detail', pk=post.pk)
        elif 'like' in request.POST:
            if not is_liked:
                Like.objects.create(post=post, user=request.user)
            else:
                post.likes.filter(user=request.user).delete()
            return redirect('blog_post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'likes': likes
    }
    return render(request, 'blog_post_detail.html', context)
