#Services URLs
from django.urls import path
from services import views
from services.views import ServiceListView, ServiceDetailsView
from services.views import ServiceCreateView, ServiceUpdateView, ServiceDeleteView 

services_urlpatterns = ([
    #path('', views.services, name='services'),
    path('', ServiceListView.as_view(), name='service_list'),
    path('pedido/', views.realizar_pedido, name="detalle_pedido"),
    path('detail/<pk>',ServiceDetailsView.as_view(), name='service_detail'),
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('update/<pk>', ServiceUpdateView.as_view(), name='update'),
    path('<pk>/delete/', ServiceDeleteView.as_view(), name='delete'),
    #path('create/', views.create, name='create'),
    #path('update/<int:service_id>', views.update, name='update'),
    #path('delete/<int:service_id>', views.delete, name='delete'),
], 'services')
