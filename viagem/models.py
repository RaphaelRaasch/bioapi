from django.db import models
from motoristas.models import Motoristas
from clientes.models import Cliente

class Viagem(models.Model):
    motorista = models.ForeignKey(Motoristas, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lat = models.CharField('Latitude', max_length=155)
    lng = models.CharField('Longitude', max_length=155)

    def __str__(self):
        return self.motorista
