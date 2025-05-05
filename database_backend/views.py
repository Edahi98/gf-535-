from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from database_backend.models import ArticuloModel, TipoArticuloModel, NotaModel
from database_backend.serializers import ArticuloSerializer, TipoArticuloSerializer, NotaSerializer, UserSerializer, \
    TipoArticuloWithIdAndNombreSerializer, TipoArticuloWithImagenAndNombreSerializer, ArticuloDetallesSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ArticuloDetallesSerializeDetail(ListModelMixin, GenericAPIView):
    queryset = ArticuloModel.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = ArticuloDetallesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TipoArticuloWithIdAndNombreViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = TipoArticuloWithIdAndNombreSerializer
    queryset = TipoArticuloModel.objects.all()

class TipoArticuloWithImagenAndNombreViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = TipoArticuloWithImagenAndNombreSerializer
    queryset = TipoArticuloModel.objects.all()

class ArticuloViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = ArticuloSerializer
    queryset = ArticuloModel.objects.prefetch_related("notas").all()


class TipoArticuloViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = TipoArticuloSerializer
    queryset = TipoArticuloModel.objects.prefetch_related("articulos").all()


class NotaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication, BasicAuthentication]
    serializer_class = NotaSerializer
    queryset = NotaModel.objects.all()