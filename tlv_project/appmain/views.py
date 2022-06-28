from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render
from .forms import ProveedorForm, ContactForm, ReclamoForm
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

def reclamo(request):
    return render(request, 'appmain/reclamo.html')

def recibido(request):
    #if request == "GET":
    datos = request.GET
    nombre = datos["nombre"]
    email = datos["email"]
    comentario = datos["reclamo"]
    print(nombre, email,comentario)
    return render(request, 'appmain/reclamo.html', {"mensaje": 'Datos Recibidos', 'nombre':nombre, 'email': email, 'comentario': comentario})

def contacto(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data['nombre']
            email= form.cleaned_data['email']
            cuerpo= form.cleaned_data['cuerpo']
            print(nombre, email, cuerpo)
    form= ContactForm()
    return render(request,'appmain/contacto.html', {'form': form})

#podemos crear un reclamo y enviarlo al admin, por medio del front de cliente. Esto se hace con form.save()
def reclamo_detail(request):
    if request.method == 'POST':
        form= ReclamoForm(request.POST)
        if form.is_valid():
            nombre= form.cleaned_data['nombre']
            cuerpo= form.cleaned_data['cuerpo']
            print(nombre, cuerpo, "Funciona")
            form.save()
    form= ReclamoForm()
    return render(request,'appmain/contacto.html', {'form': form})

def obtenerClientes(request):
    clientes= Cliente.objects.raw('select * from appmain_cliente')
    for c in clientes:
        print(c.rut, c.nombre, c. apellido)
    print(clientes)
    return render(request,'appmain/obtenerClientes.html')

def obtenerClientesv2(request):
    clientes= Cliente.objects.all()
    for c in clientes:
        print(c.rut, c.nombre, c.apellido)
    print(clientes)
    