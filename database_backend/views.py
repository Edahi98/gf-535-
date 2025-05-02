from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from database_backend.models import ArticuloModel, TipoArticuloModel, NotaModel
from database_backend.serializers import ArticuloSerializer, TipoArticuloSerializer, NotaSerializer


class ArticuloViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ArticuloSerializer
    queryset = ArticuloModel.objects.all()

class TipoArticuloViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = TipoArticuloSerializer
    queryset = TipoArticuloModel.objects.all()

class NotaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = NotaSerializer
    queryset = NotaModel.objects.all()