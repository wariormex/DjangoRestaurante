#Services URLs
from django.urls import path
from services import views

services_urlpatterns = ([
    path('', views.services, name='services'),
], 'services')
