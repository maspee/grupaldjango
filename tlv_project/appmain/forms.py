from django import forms
from django.db.models import fields
from .models import Proveedor, Reclamo

class InfoForm(forms.Form):
    pass

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('rut','razon_social','contacto','telefono','correo')

#este formulario no esta ligado a ningun modelo.
class ContactForm(forms.Form):
    nombre= forms.CharField()   
    email= forms.EmailField(label='Email')
    categoria= forms.ChoiceField(choices=[('pregunta','Pregunta'), ('emergencia', 'Emergencia'), ('otros', 'Otros')])
    tema= forms.CharField(required=False)
    cuerpo= forms.CharField(widget=forms.Textarea)

#este formulario esta ligado al modelo Reclamos. Este formulario ligado nos valida q tenemos la funcion de guardar los elementos que se crean. Se crean sobre un formulario.
class ReclamoForm(forms.ModelForm):
    class Meta:
        model= Reclamo
        fields= {'nombre', 'cuerpo'}