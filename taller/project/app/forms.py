from django import forms
from .models import Edificio, Departamento


class EdificioForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']

    def clean_ciudad(self):
        ciudad = self.cleaned_data.get('ciudad')
        if ciudad[0].upper() == 'L':
            raise forms.ValidationError(
                "El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return ciudad


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo > 100000:
            raise forms.ValidationError(
                "El costo del departamento no puede ser mayor a $100,000")
        return costo

    def clean_numero_cuartos(self):
        numero_cuartos = self.cleaned_data.get('numero_cuartos')
        if numero_cuartos <= 0 or numero_cuartos > 7:
            raise forms.ValidationError(
                "Número de cuartos no puede ser 0, ni mayor a 7")
        return numero_cuartos

    def clean_nombre_propietario(self):
        nombre_propietario = self.cleaned_data.get('nombre_propietario')
        if len(nombre_propietario.split()) < 3:
            raise forms.ValidationError(
                "El nombre completo del propietario debe tener al menos 3 palabras")
        return nombre_propietario
