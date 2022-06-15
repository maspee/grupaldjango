from django import forms
from django.db.models import fields
from .models import Proveedor

class InfoForm(forms.Form):
    pass

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('rut','razon_social','contacto','telefono','correo')