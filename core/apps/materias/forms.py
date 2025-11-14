from django import forms
from .models import Materias

class MateriasForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = [
            "nombre",
            "numero_creditos",
            "nivel",
            "horas_semana",
            "jornada",
            "imagen",
            "docentes",
        ]
        widgets = {
            "descripcion": forms.Textarea(
                attrs={"rows": 4, "cols": 40}
            ), 
        }
