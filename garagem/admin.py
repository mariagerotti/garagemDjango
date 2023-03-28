from django.contrib import admin

from .models import Acessorio, Categoria, Marca

admin.site.register(Acessorio)
admin.site.register(Categoria)
admin.site.register(Marca)