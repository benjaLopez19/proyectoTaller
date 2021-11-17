from django import forms

class FormularioBusqueda(forms.Form):
    entrada=forms.CharField()
    checkbox1=forms.CheckboxInput()
    checkbox2=forms.CheckboxInput()