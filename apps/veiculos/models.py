from django.db import models

from apps.clientes.models import Cliente

class Veiculo(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="veiculos",
        verbose_name="Proprietário"
    )

    placa = models.CharField(
        max_length=10,
        unique=True,
    )

    marca = models.CharField(
        max_length=50,
    )

    modelo = models.CharField(
        max_length=50,
    )

    cor = models.CharField(
        max_length=30,
    )

    ano = models.PositiveIntegerField()

    observacoes = models.TextField(
        blank=True,
    )

    ativo = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"{self.placa} - {self.modelo}"