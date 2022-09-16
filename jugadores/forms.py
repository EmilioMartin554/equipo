from errno import EADDRNOTAVAIL
from django import forms
class plantelFormulario(forms.Form):
    nombre=forms.CharField()
    edad=forms.CharField()
    posicion=forms.CharField()
    peso=forms.CharField()
    goles=forms.CharField()