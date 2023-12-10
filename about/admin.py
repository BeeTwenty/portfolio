from django.contrib import admin
from .models import Education, Experience, Skills, About

# Register your models here.
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(About)