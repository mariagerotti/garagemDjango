from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router


from rest_framework.routers import DefaultRouter

from garagem.views import (
    AcessorioViewSet,
    CategoriaViewSet,
    CorViewSet,
    MarcaViewSet,
    ModeloViewSet,
    VeiculoViewSet,
)

router = DefaultRouter()
router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
