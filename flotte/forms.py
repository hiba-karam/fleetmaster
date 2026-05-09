from django import forms
from .models import Vehicule

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['immatriculation', 'modele', 'kilometrage', 'etat', 'date_fabrication']
        widgets = {
            'immatriculation': forms.TextInput(attrs={'class': 'form-control'}),
            'modele': forms.Select(attrs={'class': 'form-select'}),
            'kilometrage': forms.NumberInput(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
            'date_fabrication': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }