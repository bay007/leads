from django.db import models
from django.db.models.fields import EmailField


class Leads(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=60)
    subject = models.CharField(verbose_name="Asunto", max_length=25)
    message = models.TextField(verbose_name="Mensaje", max_length=400)

    def __str__(self) -> str:
        return self.name
