from django import forms
from apps.galeria.models import Fotografia


class FotografiaForms(forms.ModelForm):
    '''Formulário de fotografia'''
    class Meta:
        model = Fotografia # Modelo de fotografia
        exclude = ["publicada", ] # Campos a serem excluídos
        labels = {
            "descricao": "Descrição", # Label do campo
            "data_adicao": "Data de registro", # Label do campo
            "usuario": "Usuário" # Label do campo
        }
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}), # Campo de nome
            'legenda': forms.TextInput(attrs={'class': 'form-control'}), # Campo de legenda
            'categoria': forms.Select(attrs={'class': 'form-control'}), # Campo de categoria
            'descricao': forms.Textarea(attrs={'class': 'form-control'}), # Campo de descrição
            'foto': forms.FileInput(attrs={'class': 'form-control'}), # Campo de foto
            'data_adicao': forms.DateTimeInput( # Campo de data de adição
                attrs={
                    'type': 'datetime-local', # Tipo de campo
                    'class': 'form-control', # Classe do campo       
                },
                format='%d/%m/%Y %H:%M', # Formato da data      
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}), # Campo de usuário
        }