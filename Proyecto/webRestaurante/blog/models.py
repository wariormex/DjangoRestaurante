from distutils.command.upload import upload
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Categoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title= models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicacion")
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name = "Autor", on_delete=models.CASCADE)
    
    
    categories = models.ManyToManyField(Category,verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
    
    def get_nombre(self):
        return self.author.first_name
    get_nombre.short_description = 'Nombre autor'