from django.db import models
from api.models import Meta

class Tarefa(models.Model):
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE, related_name='tarefas')
    concluido = models.BooleanField(default=False)
    descricao = models.TextField()