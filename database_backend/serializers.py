from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import TipoArticuloModel, ArticuloModel, NotaModel

class TipoArticuloSerializer(ModelSerializer):
    class Meta:
        model = TipoArticuloModel
        fields = "__all__"

class ArticuloSerializer(ModelSerializer):
    articulo_tipos = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ArticuloModel
        fields = "__all__"

class NotaSerializer(ModelSerializer):
    articulos = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = NotaModel
        fields = "__all__"
