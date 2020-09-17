from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from biotrack.customtoken import CustomAuthToken
from caminhoes.views import CaminhaoViewSet
from clientes.views import ClienteViewSet
from motoristas.views import MotoristaViewSet
from mtr.views import MtrViewSet
from mtritem.views import MtrItemViewSet
from sequencia.views import SequenciaViewset
from usuarios.views import UserViewSet 
from viagem.views import ViagemViewSet

router = routers.DefaultRouter()
router.register(r'mtrs', MtrViewSet)
router.register(r'mtritems', MtrItemViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'usuarios', UserViewSet)


router.register(r'sequencias', SequenciaViewset)
router.register(r'motoristas', MotoristaViewSet)
router.register(r'caminhoes', CaminhaoViewSet)
router.register(r'viagem', ViagemViewSet)



urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth-token/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
