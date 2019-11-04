from django.db import models

class Meta(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.TextField(blank=True)
    prazo = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome