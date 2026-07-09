from django.db import models

from apps.clientes.models import Cliente
from apps.veiculos.models import Veiculo


class OrdemServico(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="ordens_servico",
    )

    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name="ordens_servico",
    )

    data_entrada = models.DateTimeField(
        auto_now_add=True,
    )

    data_saida = models.DateTimeField(
        null=True,
        blank=True,
    )

    STATUS = [

        ("Aguardando", "Aguardando"),

        ("Em andamento", "Em andamento"),

        ("Finalizado", "Finalizado"),

        ("Entregue", "Entregue"),

    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Aguardando",
    )

    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    observacoes = models.TextField(
        blank=True,
    )

    def __str__(self):

        return f"OS #{self.id} - {self.veiculo}"