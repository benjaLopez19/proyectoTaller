from django import forms

class FormularioBusqueda(forms.Form):
    entrada=forms.CharField(label="", max_length=1000, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Busqueda"}))
    esRespuesta=forms.BooleanField(label="Incluir respuestas del bot", required=False)
