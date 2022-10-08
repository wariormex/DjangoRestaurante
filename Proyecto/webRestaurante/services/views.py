from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Service
from .forms import ServiceForm

def services(request):
    services = Service.objects.all()
    return render(request,'services/service_list.html', {'services':services})

@staff_member_required()
def create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            new_service = form.save()
            return HttpResponseRedirect('/')
        #else:
        #    return render(request,'services/service_form.html', {'form':form})
    else:
        form = ServiceForm()
    #return render(request,'services/service_form.html',{'form':form})
    return render(request,'services/service_create_form.html',{'form':form})

@staff_member_required()
def update(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ServiceForm()
    return render(request,'services/service_update_form.html',{'form':form})
