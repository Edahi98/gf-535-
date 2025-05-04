from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import ArticuloModel, TipoArticuloModel, NotaModel
# Register your models here.
TokenAdmin.raw_id_fields = ["user"]
class ArticuloAdmin(admin.ModelAdmin):
    sortable_by = "nombre"
    list_display = ["id", "nombre", "imagen"]
class TipoArticuloAdmin(admin.ModelAdmin):
    sortable_by = "nombre"
    list_display = ["id", "nombre", "imagen"]
class NotaAdmin(admin.ModelAdmin):
    sortable_by = "titulo"

admin.site.register(ArticuloModel, ArticuloAdmin)
admin.site.register(TipoArticuloModel, TipoArticuloAdmin)
admin.site.register(NotaModel, NotaAdmin)
