from django import forms

class FormularioBusqueda(forms.Form):
    entrada=forms.CharField(label="Introduzca busqueda", max_length=1000000, widget=forms.TextInput(attrs={}))
    esRespuesta=forms.BooleanField(label="Seleccione para buscar en las respuesta del bot", required=False)
