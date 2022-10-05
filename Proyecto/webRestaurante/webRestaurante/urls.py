"""webRestaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from . import settings
from core.urls import core_urlpatterns
from blog.urls import blog_urlpatterns
from services.urls import services_urlpatterns
from pages.urls import pages_urlpatterns
from contact.urls import contact_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('core.urls')),
    path('', include(core_urlpatterns)),
    #path('', views.home, name='home'),
    # path('historia/', views.about, name='about'),
    #path('servicios/', views.services, name='services'),
    path('servicios/', include(services_urlpatterns)),
    #path('visitanos/', views.store, name='store'),
    path('contacto/', include(contact_urlpatterns)),
    #path('blog/', views.blog, name='blog'),
    path('blog/', include(blog_urlpatterns)),
    path('pages/', include(pages_urlpatterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    