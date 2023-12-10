from django.shortcuts import render
from .models import Experience, Education, Skills, About

def about(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skills.objects.all()
    about = About.objects.all()
    return render(request, 'about.html', {'experiences': experiences, 'educations': educations, 'Skills': skills, 'about': about})
