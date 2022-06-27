from django.shortcuts import redirect, render
from django.template import ContextPopException
from .models import Publicacion
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
 
def home(request):
    contexto= {
        'posts': Publicacion.objects.all()
    }
    return render(request, 'blog/home.html', contexto)

# Create your views here.

class PublicacionDetalle(DetailView):
    model= Publicacion
    template_name= 'blog/publicacion_detalle.html'

class PublicacionCrear(LoginRequiredMixin, CreateView):
    model= Publicacion
    fields= ['titulo', 'contenido']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PublicacionActualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model= Publicacion
    fields= ['titulo', 'contenido']

    def test_func(self):
        publicacion= self.get_object()
        if self.request.user == publicacion.autor:
            return True
        return False

class PublicacionEliminar(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model= Publicacion
    template_name= 'blog/publicacion_eliminar.html'
    success_url= ''
    def test_func(self):
        publicacion= self.get_object()
        if self.request.user == publicacion.autor:
            return True
        return False
 