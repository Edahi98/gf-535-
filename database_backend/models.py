from django.db.models import (
    Model,
    TextField,
    ForeignKey,
    CASCADE,
    AutoField
)
from django.contrib import admin
from django.utils.html import format_html
# Create your models here.

class TipoArticuloModel(Model):
    id = AutoField(primary_key=True, auto_created=True)
    nombre = TextField(null=False)
    url_imagen = TextField(null=False)
    id_imagen = TextField(null=False)

    @admin.display
    def imagen(self):
        return format_html(
            '<img src="{}" alt="" style="border-radius: 20px; width: 50px;">',
            self.url_imagen
        )

class ArticuloModel(Model):
    id = AutoField(primary_key=True, auto_created=True)
    nombre = TextField(null=False)
    url_imagen = TextField(null=False)
    id_imagen = TextField(null=False)
    id_articulo_tipo = ForeignKey(TipoArticuloModel, related_name="articulo_tipos", on_delete=CASCADE)

    @admin.display
    def imagen(self):
        return format_html(
            '<img src="{}" alt="" style="border-radius: 20px; width: 50px;">',
            self.url_imagen
        )

class NotaModel(Model):
    id = AutoField(primary_key=True, auto_created=True)
    titulo = TextField(null=False)
    descripcion = TextField(null=False)
    id_articulo = ForeignKey(ArticuloModel, related_name="articulos", on_delete=CASCADE)
