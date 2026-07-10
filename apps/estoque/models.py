from django.db import models


class Produto(models.Model):

    nome = models.CharField(
        max_length=100,
    )

    quantidade = models.PositiveIntegerField()

    unidade = models.CharField(
        max_length=20,
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    fornecedor = models.CharField(
        max_length=100,
        blank=True,
    )

    ativo = models.BooleanField(
        default=True,
    )

    def __str__(self):

        return self.nome