from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from garagem.serializers import CategoriaSerializer, MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
