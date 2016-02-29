from django import forms

from .models import *

class AsistenteForm(forms.ModelForm):
       class Meta:
        model = Asistente
        fields = ['nombre', 'cedula', 'email', 'certificadoImpreso', 'evento']