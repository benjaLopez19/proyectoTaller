from django import forms

class FormularioBusqueda(forms.Form):
<<<<<<< HEAD
    entrada=forms.CharField(label="Introduzca busqueda", max_length=200, widget=forms.TextInput(attrs={}))
    esRespuesta=forms.BooleanField(label="Seleccione para buscar en las respuesta del bot", required=False)
=======
    entrada=forms.CharField(label="Introduzca busqueda", max_length=1000000, widget=forms.TextInput(attrs={}))
    esRespuesta=forms.BooleanField(label="Seleccione para buscar en las respuesta del bot", required=False)
>>>>>>> e12c0184f3be1df7d113ec0239fc0d4cd5e534ad
