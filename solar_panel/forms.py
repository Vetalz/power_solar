from django import forms
from .models import *


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control mb-3'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Ваш номер телефона', 'class': 'form-control mb-3'}),
        }
