from django.shortcuts import render
from projects.models import Project



def home(request):
    latest_project = Project.objects.order_by('-date_added').first()
    projects = Project.objects.all()
    context = {
        'latest_project': latest_project,
        'projects': projects
    }
    return render(request, 'home.html', context)