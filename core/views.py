from django.shortcuts import render
from projects.models import Project
from .models import info_one, info_two
from blog.models import BlogPost
import markdown

def home(request):
    latest_project = Project.objects.order_by('-date_added').first()
    projects = Project.objects.all()
    info1 = info_one.objects.first()
    info2 = info_two.objects.first()
    latest_blog = BlogPost.objects.order_by('-date_posted').first()
    if latest_blog:
        latest_blog.content = markdown.markdown(latest_blog.content)
    context = {
        'latest_project': latest_project,
        'projects': projects,
        'info1': info1,
        'info2': info2,
        'latest_blog': latest_blog
    }
    return render(request, 'home.html', context)
