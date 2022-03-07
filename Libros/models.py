from django.db import models

# Create your models here.
class Autor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    birth_date = models.DateField()

def get_name(self):
        return self.nombres + " " + self.apellidos

class Book(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    year = models.IntegerField()
    cost = models.IntegerField()
    author =  models.ForeignKey(Autor, on_delete=models.CASCADE)