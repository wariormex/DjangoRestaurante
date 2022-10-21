from django.contrib import admin
from .models import Service, Pedido

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_display = ('name', 'total')
    
admin.site.register(Service, ServiceAdmin)
admin.site.register(Pedido, PedidoAdmin)
