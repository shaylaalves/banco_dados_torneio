from django.db import models
from django.core.exceptions import ValidationError

class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    idade = models.IntegerField()
    ranking = models.IntegerField()

    class Meta:
        unique_together = ('nome', 'cidade')

    def __str__(self):
        return self.nome


class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.IntegerField()
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} (Nv. {self.nivel})"

    def clean(self):
        if not (1 <= self.nivel <= 100):  
            raise ValidationError({'nivel': 'O nível deve estar entre 1 e 100.'})
    


class Batalha(models.Model):
    data = models.DateField()
    local = models.CharField(max_length=100)
    vencedor = models.ForeignKey(Treinador, on_delete=models.CASCADE, related_name='vitorias')
    perdedor = models.ForeignKey(Treinador, on_delete=models.CASCADE, related_name='derrotas')

    def __str__(self):
        return f"{self.vencedor} vs {self.perdedor} - {self.data}"


class Item(models.Model):
    nome = models.CharField(max_length=100)
    efeito = models.TextField()
    quantidade = models.PositiveIntegerField()
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.quantidade}x)"


class Time(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    treinadores = models.ManyToManyField(Treinador)

    def __str__(self):
        return self.nome


class Local(models.Model):
    nome = models.CharField(max_length=100, unique=True) 
    tipo_ambiente = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class TreinadorTime(models.Model):
    treinador = models.ForeignKey(Treinador, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('treinador', 'time')  # ✅ chave composta

    def __str__(self):
        return f"{self.treinador} - {self.time}"
