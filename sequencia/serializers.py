
from rest_framework.serializers import ModelSerializer
from .models import Sequencia
from clientes.serializers import ClienteSerializer


class SequenciaSerializers(ModelSerializer):

    #

    class Meta:
        model = Sequencia
        fields = ('numero', 'mtr', 'cliente', 'rua', 'numero', 'bairro', 'municipio', 'estado', 'lat', 'long')
