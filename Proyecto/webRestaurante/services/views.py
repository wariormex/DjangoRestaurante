from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Service
from .forms import ServiceForm

class ServiceListView(ListView):
    model = Service
    paginate_by = 1

class ServiceDetailsView(DetailView):
    model = Service 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now() 
        return context
    
class ServiceCreateView(CreateView):
    model = Service
    fields = ['title', 'subtitle', 'content', 'image']
    template_name_suffix = '_create_form'
    
    success_url = reverse_lazy('services:service_list')
    
class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['title', 'subtitle', 'content', 'image']
    template_name_suffix = '_update_form'
    
    success_url = reverse_lazy('services:service_list')
   
class ServiceDeleteView(DeleteView):
    model = Service
    template_name_suffix = '_delete_form'
    
    success_url = reverse_lazy('services:service_list')
 
def _creaDiccionario(datos_pedido):
    diccionario = {}
    datos_pedido = datos_pedido[:-1]
    productos = datos_pedido.split('|')
    for producto in productos:
        detalle = producto.split('-')
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario

def realizar_pedido(request):
    pedido = list()
    if request.method == 'POST':
        datos_pedido = request.POST['datos_pedido']
        print(datos_pedido)
        productos = _creaDiccionario(datos_pedido)
        total = 0
        for key in productos.keys():
            cantidad = productos[key]
            if cantidad > 0:
                dict_producto = {}
                servicio = Service.objects.get(pk=key)
                dict_producto['titulo'] = servicio.title
                dict_producto['subtitulo'] = servicio.subtitle
                dict_producto['cantidad'] = cantidad
                dict_producto['precio'] = "100"
                total += cantidad * 100
                pedido.append(dict_producto)
        request.session['total_float'] = float(total)
        request.session['detalle_pedido'] = pedido
        print(pedido,total)
    return render(request, 'services/detalle_pedido.html',{"pedido":pedido, "total":total})               
         
         
                
'''   
def services(request):
    services = Service.objects.all()
    return render(request,'services/service_list.html', {'services':services})

@staff_member_required()
def create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            new_service = form.save()
            return HttpResponseRedirect('/servicios/')
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
            return HttpResponseRedirect('/servicios/')
    else:
        form = ServiceForm()
    return render(request,'services/service_update_form.html',{'form':form})

@staff_member_required()
def delete(request, service_id):
    context = {}
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        service.delete()
        return HttpResponseRedirect('/servicios/')
    return render(request,'services/service_delete_form.html',context)
'''