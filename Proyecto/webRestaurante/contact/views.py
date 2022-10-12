from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .forms import ContactForm
from django.urls import reverse_lazy
import time
from blog.models import Category

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            pos_arroba = email.find('@')
            dominio = email[pos_arroba+1:]
            
            if dominio != "gmail.com":
                form.add_error('email','dominio invalido')
                return render(request,'contact/contact.html',{'form':form})
            #print(form.cleaned_data.get('name'))
            #print(form.cleaned_data['email'])
            #return HttpResponseRedirect('/contact/thanks/')
            
            return HttpResponseRedirect(reverse_lazy('contact:thanks'))
    else: 
        form = ContactForm()
    return render(request, 'contact/contact.html',{'form':form})
    
def thanks(request):
    return render(request, 'contact/thanks.html')

#Practica AJAX
def ejecutaAJAX(request):
    if request.method == 'POST':
        #Validacion de campos
        categorias = Category.objects.all()
        opcion = request.POST.get('valor','')
        respuesta = {}
        opciones = {}
        if opcion == '1':
            respuesta['estado'] = 'correcto'
            for categoria in categorias:
                opciones[categoria.id] = categoria.name
            #opciones['1'] = 'Opcion1'
            #opciones['2'] = 'Opcion2'
            #opciones['3'] = 'Opcion3'
            #opciones['4'] = 'Opcion4'
            #opciones['5'] = 'Opcion5'
        elif opcion == '2':
            respuesta['estado'] = 'correcto'
            opciones['1'] = '2 - Opcion1'
            opciones['2'] = '2 - Opcion2'
            opciones['3'] = '2 - Opcion3'
        else:
            respuesta['estado'] = 'No valido'
            
        respuesta['opciones'] = opciones
        time.sleep(5)
        return JsonResponse(respuesta)
            

# Create your views here.
