from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView

from .models import Autor, Book
from .forms import AuthorForm

# Create your views here.

def index(request):
    template = loader.get_template('autores/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

#Vista para listar autores
def listarAutores(request):
    lista = Autor.objects.all()
    output = ', '.join([a.nombres for a in lista])
    return HttpResponse(output) 

#vista para crear autores.
def create_autor(request):

    context = {}

    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('autores')
    
    context['form'] = form
    return render(request,'autores/create_autor.html', context)

#Vista para ver detalles de un autor
def detail_view(request, id):
    context = {}

    context['object'] = Autor.objects.get(id = id)

    return render(request,'autores/autor_detalle.html',context)

#vista para actualizar autores
#Referencia https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/?ref=lbp
def update_autor(request,id):

    context = {}

    obj = get_object_or_404(Autor, id = id)

    #formulario que contendra la instancia
    form = AuthorForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('autores')
    
    context['form'] = form

    return render(request, "autores/update_view.html", context)

#Vista para eliminar un autor
def delete_view(request, id):

    context = {}

    obj = get_object_or_404(Autor, id = id)

    if request.method == "POST":
        obj.delete()
        return redirect('autores')
    
    return render(request, "autores/delete_view.html", context)


def listarBooks(request):
    lista = Book.objects.all()
    output = ', '.join([a.nombre for a in lista])
    return HttpResponse(output) 