from django import forms

class FormularioBusqueda(forms.Form):
    entrada=forms.CharField(label="Introduzca busqueda", max_length=200)
    checkbox1=forms.BooleanField()
    checkbox2=forms.CheckboxInput()