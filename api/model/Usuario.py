from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome = models.CharField()
    matricula = models.IntegerField()
    gerente = models.BooleanField(default=False)
    funcao = models.CharField(blank=True)

    USERNAME_FIELD = matricula



    