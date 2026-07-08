from django.db import models


class Cliente(models.Model):

    nome = models.CharField(
        max_length=150
    )

    cpf = models.CharField(
        max_length=14,
        unique=True
    )

    telefone = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    endereco = models.CharField(
        max_length=200,
        blank=True
    )

    cidade = models.CharField(
        max_length=100,
        blank=True
    )

    estado = models.CharField(
        max_length=2,
        blank=True
    )

    cep = models.CharField(
        max_length=9,
        blank=True
    )

    observacoes = models.TextField(
        blank=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nome