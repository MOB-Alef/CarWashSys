from django import forms

from .models import Funcionario


class FuncionarioForm(forms.ModelForm):

    class Meta:

        model = Funcionario

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

            "cargo": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "salario": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),

            "ativo": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),

        }