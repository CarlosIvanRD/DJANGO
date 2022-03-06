from django.contrib import admin

# Register your models here.
from .models import Autor
from .models import Book
admin.site.register(Autor)
admin.site.register(Book)