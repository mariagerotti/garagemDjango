from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from garagem.serializers import CategoriaSerializer, CorSerializer, MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
    
class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
