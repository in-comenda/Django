from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    idade = models.IntegerField


def __str__(self):
    return self.nome
