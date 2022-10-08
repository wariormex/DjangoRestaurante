from django import forms
from django.forms import ModelForm, TextInput, Textarea
from services.models import Service 

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