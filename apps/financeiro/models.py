from django.db import models


class Movimentacao(models.Model):

    TIPO_CHOICES = [
        ("Entrada", "Entrada"),
        ("Saída", "Saída"),
    ]

    descricao = models.CharField(
        max_length=100
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    data = models.DateField()

    observacoes = models.TextField(
        blank=True
    )

    def __str__(self):

        return f"{self.descricao} - R$ {self.valor}"