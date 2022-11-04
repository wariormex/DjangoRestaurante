from django.test import TestCase
from .models import Pedido, Service
from django.urls import reverse

class ServiceModelTests(TestCase):
    def test_not_empty(self):
        pedido = Pedido(
            name = 'Pedido 1',
            address = 'Dirección 1',
            colony = 'Colonia 1',
            total = 750.34,
            email = 'fvazquez@anahuac.mx')
        Pedido.save(pedido)
        pedidos = Pedido.objects.all()
        self.assertIs(len(pedidos)>0, True)
        self.assertEquals(pedidos[0].name, 'Pedido 1')
        print(pedidos[0].date)
        
    def test_service_list(self):
        service1 = Service(
            title = 'Servicio 1',
            subtitle = 'Subtitulo 1',
            content = 'Prueba de contenido',
            image = '/services/imagen1.jpg'
        )
        Service.save(service1)
        
        service2 = Service(
            title = 'Servicio 2',
            subtitle = 'Subtitulo 2',
            content = 'Prueba de contenido',
            image = '/services/imagen2.jpg'
        )
        Service.save(service2)
        
        response = self.client.get(reverse('services:service_list'))
        self.assertQuerysetEqual(
            response.context['object_list'],
            #[service1,service2]   
            [service1]                
        )
