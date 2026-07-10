from django import forms

from .models import Movimentacao


class MovimentacaoForm(forms.ModelForm):

    class Meta:

        model = Movimentacao

        fields = "__all__"

        widgets = {

            "descricao": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "tipo": forms.Select(attrs={
                "class": "form-select",
            }),

            "valor": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),

            "data": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "observacoes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),

        }