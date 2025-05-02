from django.db.models import (
    Model,
    TextField,
    ForeignKey,
    CASCADE,
    AutoField
)
from uuid import uuid4
# Create your models here.

class TipoArticuloModel(Model):
    id = AutoField(primary_key=True, auto_created=True)
    nombre = TextField(null=False)
    url_imagen = TextField(null=False)
    id_imagen = TextField(null=False)

class ArticuloModel(Model):
    id = AutoField(primary_key=True, auto_created=True)
    nombre = TextField(null=False)
    url_imagen = TextField(null=False)
    id_imagen = TextField(null=False)
    id_articulo_tipo = ForeignKey(TipoArticuloModel, related_name="articulo_tipos", on_delete=CASCADE)

class NotaModel(Model):
    id = AutoField(primary_key=True, auto_created=True)
    titulo = TextField(null=False)
    descripcion = TextField(null=False)
    id_articulo = ForeignKey(ArticuloModel, related_name="articulos", on_delete=CASCADE)