from django.contrib import admin
from . models import Cliente, Proveedor, Reclamo

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Reclamo)