from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Acessório"


class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Cores"


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


class Veiculo(models.Model):
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
