from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views as views_api

router = DefaultRouter()
router.register(r"articulos", views_api.ArticuloViewSet)
router.register(r"tipos_articulos", views_api.TipoArticuloViewSet)
router.register(r"notas", views_api.NotaViewSet)
router.register(r"usuarios", views_api.UserViewSet)

urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token),
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls))
]