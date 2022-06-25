from re import template
from django.urls.resolvers import URLPattern
from django.urls import path
from . import views


urlpatterns = [
    path('', views.yaru, name ='appmain' ),
    path('clientes/', views.clientes, name='appmain-clientes'),
    path('proveedor/', views.proveedor, name='appmain-proveedor'),
    path('reclamo/', views.reclamo, name= 'appmain-reclamo'),
    path('recibido/', views.recibido), 
    path('contacto/', views.contacto, name= 'appmain-contacto'), 
    path('reclamo_detail/', views.reclamo_detail)    
     
]
