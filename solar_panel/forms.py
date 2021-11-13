from django import forms
from .models import *


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'form-control mb-3', 'id': 'form_name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Ваш номер телефона', 'class': 'form-control mb-3',
                                                   'id': 'form_phone'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['method_delivery', 'name', 'phone', 'region', 'city', 'new_post_office',
                  'address', 'comment', 'method_payment', 'product']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control", "id": "input-name", "aria-describedby": "nameHelp",
                                   "placeholder": "ФИО"}),
            'phone': forms.TextInput(attrs={"class": "form-control", "id": "input-phone",
                                            "aria-describedby": "nameHelp"}),
            'region': forms.Select(attrs={"class": "form-control form-select", "id": "input-region",
                                    "aria-describedby": "nameHelp"}),
            'city': forms.TextInput(attrs={"class": "form-control", "id": "input-city", "aria-describedby": "nameHelp",
                                      "placeholder": "Город"}),
            'new_post_office': forms.NumberInput(attrs={"class": "form-control", "id": "input-new_post",
                                                  "aria-describedby": "nameHelp",
                                                  "placeholder": "№ отделения Новой Почты"}),
            'address': forms.TextInput(attrs={"class": "form-control", "id": "input-address", "aria-describedby": "nameHelp",
                                      "placeholder": "Домашний адрес для курьерской доставки"}),
            'comment': forms.TextInput(attrs={"class": "form-control", "id": "input-comment", "aria-describedby": "nameHelp",
                                      "placeholder": "Комментарий по желанию"}),
            'product': forms.HiddenInput(attrs={"id": "input-equipment"})
        }
