from django import forms
from .models import Autor

#Crear formulario
class AuthorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Autor

        #especificar los campos
        fields = [
            'nombres',
            'apellidos',
            'birth_date'
        ]