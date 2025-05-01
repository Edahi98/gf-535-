from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UsuarioViewSet

router = SimpleRouter()
router.register("usuario", UsuarioViewSet)

urlpatterns = [
    path("", include(router.urls))
]