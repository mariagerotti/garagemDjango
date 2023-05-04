from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo
from garagem.serializers import (
    AcessorioSerializer,
    CategoriaSerializer,
    CorSerializer,
    MarcaSerializer,
    ModeloSerializer
)


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer