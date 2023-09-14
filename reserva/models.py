from django.db import models

class reserva (models.Model):
    cnpj = models.CharField(max_length=150)
    nome_empresa = models.CharField(max_length=200)
    categoria_empresa = models.CharField(max_length=250)
    quitado = models.BooleanField()


class Stand (models.Model):
    localizacao = models.CharField(max_length=300)
    valor = models.FloatField()