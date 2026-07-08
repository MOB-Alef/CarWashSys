from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:

        model = Cliente

        fields = "__all__"

        widgets = {

            "nome": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "cpf": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "telefone": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
            }),

            "endereco": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "cidade": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "estado": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "cep": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "observacoes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),

            "ativo": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),

        }