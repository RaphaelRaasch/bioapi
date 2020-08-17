from .models import Mtr
from rest_framework.serializers import ModelSerializer
from clientes.serializers import ClienteSerializer

class MtrSerializer(ModelSerializer):

    class Meta:
        model = Mtr
        fields = ('numero', 'motorista', 'alias', 'saida', 'chegada', 'caminhao')
