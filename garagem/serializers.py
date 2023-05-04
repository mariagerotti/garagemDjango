from rest_framework.serializers import ModelSerializer

from garagem.models import Acessorio, Categoria, Cor, Marca, Modelo


class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
        
class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
