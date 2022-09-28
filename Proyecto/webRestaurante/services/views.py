from django.shortcuts import render
from .models import Service

def services(request):
    services = Service.objects.all()
    return render(request,'services/service_list.html', {'services':services})
