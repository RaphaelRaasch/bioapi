from rest_framework.viewsets import ModelViewSet
from .serializers import ViagemSerializer
from .models import Viagem


class ViagemViewSet(ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer