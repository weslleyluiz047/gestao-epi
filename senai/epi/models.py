from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, default='DEFAULT_VALUE')

    def __str__(self):
        return self.nome

class EPI(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    tamanho = models.CharField(max_length=10)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"
