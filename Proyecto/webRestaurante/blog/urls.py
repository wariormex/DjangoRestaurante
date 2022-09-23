from django.urls import path
from blog import views


blog_urlpatterns = ([
    path('blog/', views.blog, name='blog'),
], 'blog')