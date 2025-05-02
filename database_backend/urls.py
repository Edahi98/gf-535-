from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from . import views as views_api

router = DefaultRouter()
router.register(r"articulos", views_api.ArticuloViewSet)
router.register(r"tipos_articulos", views_api.TipoArticuloViewSet)
router.register(r"notas", views_api.NotaViewSet)

urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token),
    path("", include(router.urls))
]