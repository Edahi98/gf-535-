from rest_framework.serializers import ModelSerializer
from .models import TipoArticuloModel, ArticuloModel, NotaModel, UsuarioModel

class TipoArticuloSerializer(ModelSerializer):
    class Meta:
        model = TipoArticuloModel
        fields = ["id", "nombre", "url_imagen", "id_imagen"]
        read_only_fields = ('id',)

class ArticuloSerializer(ModelSerializer):
    articulo_tipos = TipoArticuloSerializer(many=True)
    class Meta:
        model = ArticuloModel
        fields = ["id", "nombre", "url_imagen", "id_imagen", "articulo_tipos"]
        read_only_fields = ("id",)

class NotaSerializer(ModelSerializer):
    articulos = ArticuloSerializer(many=True)
    class Meta:
        model = NotaModel
        fields = ["id", "titulo", "descripcion", "articulos"]
        read_only_fields = ("id",)

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = ["nickname", "t2f_url", "pwd"]

