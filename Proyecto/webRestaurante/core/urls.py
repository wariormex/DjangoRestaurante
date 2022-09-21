from django.urls import path
from core import views


core_urlpatterns = ([
    path('', views.home, name='home'),
    path('historia/', views.about, name='about'),
    path('visitanos/', views.store, name='store'),
], 'core')