# api/models.py
from django.db import models

class FormResponse(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)  # Apellido
    age = models.IntegerField()
    email = models.EmailField()  # Correo electrónico
    sex = models.CharField(max_length=10)  # Sexo (puedes usar 'M' o 'F' o algo más)
    country = models.CharField(max_length=100)  # País
    occupation = models.CharField(max_length=100)  # Ocupación
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.last_name}, {self.age} años, {self.country}"
