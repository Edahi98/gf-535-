from rest_framework.serializers import ModelSerializer, IntegerField
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

class ArticuloSerializer(ModelSerializer):
    notas = NotaSerializer(many=True, read_only=True)
    class Meta:
        model = ArticuloModel
        fields = [
            "id",
            "nombre",
            "url_imagen",
            "id_imagen",
            "id_articulo_tipo"
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
            "id_imagen",
            "articulos"
        ]

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"