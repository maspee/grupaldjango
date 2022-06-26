from django.shortcuts import render
from django.template import ContextPopException
from .models import Publicacion
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
 
def home(request):
    contexto= {
        'posts': Publicacion.objects.all()
    }
    return render(request, 'blog/home.html', contexto)

# Create your views here.

class PublicacionDetalle(DetailView):
    model= Publicacion
    template_name= 'blog/publicacion_detalle.html'

class PublicacionCrear(CreateView):
    model= Publicacion
    fields= ['titulo', 'contenido']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)