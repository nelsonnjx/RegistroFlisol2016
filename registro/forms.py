from django import forms
from django.core.exceptions import NON_FIELD_ERRORS



from .models import *

class AsistenteForm(forms.ModelForm):
       class Meta:
        model = Asistente
        fields = ['nombre', 'cedula', 'email', 'evento']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

