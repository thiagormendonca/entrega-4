from django.db import models
from ..models import Tarefa, Usuario

class FuncionarioTarefa(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)