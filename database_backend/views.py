from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UsuarioSerializer
from .models import UsuarioModel

class UsuarioViewSet(ReadOnlyModelViewSet):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
