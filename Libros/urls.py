from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('autores/', views.listarAutores, name='index' ),
]