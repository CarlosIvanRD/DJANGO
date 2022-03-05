from multiprocessing.spawn import import_main_path
from django.contrib import admin
from .models import Persona

# Register your models here.


admin.site.register(Persona)