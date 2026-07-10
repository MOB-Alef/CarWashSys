from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:

        model = Produto

        fields = "__all__"

        widgets = {

            "nome": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "quantidade": forms.NumberInput(attrs={
                "class": "form-control",
            }),

            "unidade": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "preco": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),
            

            "fornecedor": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "ativo": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),

        }