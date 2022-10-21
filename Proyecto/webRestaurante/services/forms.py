from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from services.models import Service, Pedido 

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title':TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
            'subtitle':TextInput(attrs={'class':'form-control', 'placeholder':'Sub titulo'}),
        }
    #Funcion de validacion del formulario
    def clean(self):
        super(ServiceForm, self).clean()
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class(['Minimo 5 caracteres'])
        return self.cleaned_data
    
class PedidoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        total_float = self.request.session.get('total_float')
        super().__init__(*args, **kwargs)
        self.fields["total"].initial=total_float
        
    class Meta:
        model = Pedido
        fields = ['name', 'address', 'colony', 'email', 'total']
        widgets = {
            'name':TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'address':TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
            'colony':TextInput(attrs={'class':'form-control', 'placeholder':'Colonia o Fraccionamiento'}),
            'email':EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'total':TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }