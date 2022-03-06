from ast import Return
from re import A
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Autor
# Create your views here.

def index(request):
    return HttpResponse("Hola mundo")

def listarAutores(request):
    lista = Autor.objects.all()
    output = ', '.join([a.nombres for a in lista])
    return HttpResponse(output) 