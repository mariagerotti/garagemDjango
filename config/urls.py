from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet, MarcaViewSet

router = DefaultRouter()
router.register(r"Marca", MarcaViewSet)
router.register(r"Categoria", CategoriaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]