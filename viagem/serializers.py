from rest_framework.serializers import ModelSerializer
from .models import Viagem


class ViagemSerializer(ModelSerializer):

    class Meta:
        model = Viagem
        fields = '__all__'