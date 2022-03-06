from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Autor, Book
# Create your views here.

def index(request):
    return HttpResponse("Hola mundo")

def listarAutores(request):
    lista = Autor.objects.all()
    output = ', '.join([a.nombres for a in lista])
    return HttpResponse(output) 

def listarBooks(request):
    lista = Book.objects.all()
    output = ', '.join([a.nombre for a in lista])
    return HttpResponse(output) 