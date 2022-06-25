from django.shortcuts import render
from django.template import ContextPopException
from .models import Publicacion


def home(request):
    contexto= {
        'posts': Publicacion.objects.all()
    }
    return render(request, 'blog/home.html', contexto)

# Create your views here.
