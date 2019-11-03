from django.db import models

class Meta(models.Model):
    nome = models.CharField()
    descricao = models.TextField(blank=True)
    prazo = models.DateTimeField(blank=True)

    def __str__(self):
        return self.nome