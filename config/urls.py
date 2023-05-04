from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import AcessorioViewSet, CategoriaViewSet, CorViewSet, MarcaViewSet, ModeloViewSet

router = DefaultRouter()
router.register(r"Acessorio", AcessorioViewSet)
router.register(r"Categoria", CategoriaViewSet)
router.register(r"Cor", CorViewSet)
router.register(r"Marca", MarcaViewSet)
router.register(r"Modelo", ModeloViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
