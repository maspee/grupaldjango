from django.shortcuts import redirect, render
from .forms import ProveedorForm
from .models import Cliente, Proveedor


def yaru(request):
    return render(request,'appmain/home.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'appmain/clientes.html', {"data": cliente})

def proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(data= request.POST)
        if form.is_valid():
            rut=form.cleaned_data["rut"]
            razon_social=form.cleaned_data["razon_social"]
            contacto=form.cleaned_data["contacto"]
            telefono=form.cleaned_data["telefono"]
            correo=form.cleaned_data["correo"]
            print(rut,razon_social,contacto,telefono,correo)
            form.save()
            return redirect('appmain/crearproveedor.html')
    else:
        form = ProveedorForm()
        return render(request,'appmain/crearproveedor.html', {"form": form})