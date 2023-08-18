from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer

from garagem.models import Veiculo


class VeiculoSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Veiculo
        fields = "__all__"


class VeiculoDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1


class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "ano"]
