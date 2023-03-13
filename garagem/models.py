from django.db import models

class Modelo(models.Model):
    descricao = models.CharField(max_length=100)