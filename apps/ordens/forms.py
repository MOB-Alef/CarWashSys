from django import forms

from .models import OrdemServico


class OrdemServicoForm(forms.ModelForm):

    class Meta:

        model = OrdemServico

        fields = "__all__"

        widgets = {

            "cliente": forms.Select(attrs={
                "class": "form-select",
            }),

            "funcionario": forms.Select(
    attrs={
        "class": "form-select",
    }
),

            "veiculo": forms.Select(attrs={
                "class": "form-select",
            }),

            "status": forms.Select(attrs={
                "class": "form-select",
            }),

            "valor": forms.NumberInput(attrs={
                "class": "form-control",
            }),

            "observacoes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),

            "data_saida": forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local",
            }),

        }