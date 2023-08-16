from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Modelo, Marca, Veiculo
from garagem.serializers import (
    AcessorioSerializer,
    CategoriaSerializer,
    CorSerializer,
    MarcaSerializer,
    VeiculoSerializer,
    VeiculoDetailSerializer,
    VeiculoListSerializer,
    ModeloSerializer
)


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer
    
class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_classes = {
        "list": VeiculoListSerializer,
        "retrieve": VeiculoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, VeiculoSerializer)