from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse_lazy

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

# Create your views here.
