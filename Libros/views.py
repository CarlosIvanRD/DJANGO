from ast import Return
from re import A
from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor
# Create your views here.

def index(request):
    return HttpResponse("Hola mundo")

def listarAutores(request):
    lista = Autor.objects.all()
    output = ', '.join([A.nombres for q in lista])
    return HttpResponse(output)