from django.db import models

from garagem.models import Categoria, Marca

class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelos")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="modelos"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"