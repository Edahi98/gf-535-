from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import TipoArticuloModel, ArticuloModel, NotaModel
from django.contrib.auth.models import User

class NotaSerializer(ModelSerializer):
    id_articulo = PrimaryKeyRelatedField(write_only=True, queryset=NotaModel.objects.all())
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
    id_articulo_tipo = PrimaryKeyRelatedField(queryset=TipoArticuloModel.objects.all(), write_only=True)
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