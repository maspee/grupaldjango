from re import template
from django.urls.resolvers import URLPattern
from django.urls import path
from . import views
from blog.views import PublicacionDetalle, PublicacionCrear, PublicacionActualizar


urlpatterns = [
    path('', views.yaru, name ='appmain' ),
    path('clientes/', views.clientes, name='appmain-clientes'),
    path('proveedor/', views.proveedor, name='appmain-proveedor'),
    path('reclamo/', views.reclamo, name= 'appmain-reclamo'),
    path('recibido/', views.recibido), 
    path('contacto/', views.contacto, name= 'appmain-contacto'), 
    path('reclamo_detail/', views.reclamo_detail),
    path('_publicacion/<int:pk>', PublicacionDetalle.as_view(), name='publicacion-detalle'), 
    path('publicacion/new', PublicacionCrear.as_view(), name='publicacion-crear'),
    path('publicacion/<int:pk>/update/', PublicacionActualizar.as_view(), name='publicacion-actualizar') 
     
]
