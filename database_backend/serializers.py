from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import TipoArticuloModel, ArticuloModel, NotaModel
from django.contrib.auth.models import User

class NotaSerializer(ModelSerializer):
    class Meta:
        model = NotaModel
        fields = [
            "id",
            "titulo",
            "descripcion",
            "id_articulo"
        ]

class ArticuloDetallesSerializer(ModelSerializer):
    class Meta:
        model = ArticuloModel
        fields = [
            "id",
            "nombre",
            "url_imagen",
            "id_articulo_tipo"
        ]

class ArticuloSerializer(ModelSerializer):
    notas = NotaSerializer(many=True, read_only=True)
    class Meta:
        model = ArticuloModel
        fields = [
            "id",
            "nombre",
            "url_imagen",
            "id_articulo_tipo",
            "notas"
        ]

class TipoArticuloSerializer(ModelSerializer):
    articulos = ArticuloSerializer(many=True, read_only=True)
    class Meta:
        model = TipoArticuloModel
        fields = [
            "id",
            "nombre",
            "url_imagen",
            "articulos"
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TipoArticuloWithIdAndNombreSerializer(ModelSerializer):
    class Meta:
        model = TipoArticuloModel
        fields = [
            "id",
            "nombre"
        ]
class TipoArticuloWithImagenAndNombreSerializer(ModelSerializer):
    class Meta:
        model = TipoArticuloModel
        fields = [
            "url_imagen",
            "nombre"
        ]