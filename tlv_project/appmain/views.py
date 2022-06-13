from django.shortcuts import render
from .models import Cliente

def yaru(request):
    return render(request,'appmain/home.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'appmain/clientes.html', {"data": cliente})