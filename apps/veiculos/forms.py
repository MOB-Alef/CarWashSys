from django import forms

from .models import Veiculo


class VeiculoForm(forms.ModelForm):

    class Meta:

        model = Veiculo

        fields = "__all__"

        widgets = {

            "cliente": forms.Select(attrs={
                "class": "form-select",
            }),

            "marca": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "modelo": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "placa": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "ano": forms.NumberInput(attrs={
                "class": "form-control",
            }),

            "cor": forms.TextInput(attrs={
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