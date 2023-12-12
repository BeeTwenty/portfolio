from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog_index, name='blog'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
