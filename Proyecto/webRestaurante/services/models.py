from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Services
class Service(models.Model):
    title= models.CharField(max_length=200, verbose_name="Titulo")
    subtitle= models.CharField(max_length=200, verbose_name="Subtitulo")
    content = RichTextUploadingField(verbose_name="Contenido")
    image = models.ImageField(upload_to='services', null=True, blank=True)
    
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["-updated"]
        
    def __str__(self):
        return self.title
    
class Pedido(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    email = models.EmailField(verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    address = models.CharField(max_length=200, verbose_name="Calle y Numero")
    colony = models.CharField(max_length=200, verbose_name="Colonia")
    total = models.DecimalField(verbose_name="Total", max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-date"]
    
    def __str__(self):
        return str(self.id)
    
