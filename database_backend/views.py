from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from database_backend.models import ArticuloModel, TipoArticuloModel, NotaModel
from database_backend.serializers import ArticuloSerializer, TipoArticuloSerializer, NotaSerializer


class ArticuloViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticuloSerializer
    queryset = ArticuloModel.objects.all()

class TipoArticuloViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TipoArticuloSerializer
    queryset = TipoArticuloModel.objects.all()

class NotaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NotaSerializer
    queryset = NotaModel.objects.all()