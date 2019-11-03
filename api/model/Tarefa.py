from django.db import models
from api.models import Meta

class Tarefa(models.Model):
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)