from django.forms import ModelForm
from django import forms
from .models import reserva, Stand

class reservaForm(ModelForm):

    class Meta:
        model = reserva
        fields = '__all__'
        widgets = {
            'cnpj' : forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'categoria_empresa' : forms.TextInput(attrs={'class': 'form-control' }),
            'quitado': forms.Textarea(attrs={'class': 'form-control' }),
        }

class StandForm(ModelForm):

    class Meta:
        model = Stand
        fields = '__all__'
        widgets = {
            'localizacao' : forms.TextInput(attrs={'class': 'form-control' }),
            'valor' : forms.TextInput(attrs={'class': 'form-control' }),

        }