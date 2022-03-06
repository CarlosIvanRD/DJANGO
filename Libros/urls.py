from unicodedata import name
from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('autores/', views.listarAutores, name='autores' ),
    path('autores/new', views.create_autor, name='new_autor'),
    path('autores/<id>/', views.detail_view, name='autor_detail'),
    path('libros/', views.listarBooks, name='index' )
]