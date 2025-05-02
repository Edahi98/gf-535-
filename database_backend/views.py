from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from database_backend.models import ArticuloModel, TipoArticuloModel, NotaModel
from database_backend.serializers import ArticuloSerializer, TipoArticuloSerializer, NotaSerializer


class ArticuloViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ArticuloSerializer
    queryset = ArticuloModel.objects.all()

class TipoArticuloViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TipoArticuloSerializer
    queryset = TipoArticuloModel.objects.all()

class NotaViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotaSerializer
    queryset = NotaModel.objects.all()