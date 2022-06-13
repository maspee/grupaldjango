from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.yaru, name ='appmain' ),
    path('clientes/', views.clientes, name='appmain-clientes')
]
