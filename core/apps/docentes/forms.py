from django import forms
from .models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = [
            "nombre",
            "apellido",
            "correo",
            "cedula",
            "tipo_sangre",
            "direccion",
            "imagen",
        ]
        widgets = {
            "direccion": forms.Textarea(
                attrs={"rows": 4, "cols": 40}
            ),
        }
