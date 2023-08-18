from django.db import models
from uploader.models import Image


from garagem.models import Cor ,Modelo

class Veiculo(models.Model):
    capa = models.ManyToManyField(
        Image,
        related_name="+",
    )
    acessorios = models.ManyToManyField(default=None, to="Acessorio", blank=True)
    ano = models.IntegerField(default=0, null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
    )
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    descricao = models.CharField(max_length=100, default="descricao", null=True, blank=True)

    def __str__(self):
        return f"{self.marca}, ({self.ano}), ({self.cor})"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        

