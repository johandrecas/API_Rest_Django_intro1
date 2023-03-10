"""aqui es dondde crearemos el formulario para 
   recibir datos y pasarselos al modelo """


from django import forms
from .models import Autor

class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields=['nombre','apellidos','nacionalidad','descripcion']

