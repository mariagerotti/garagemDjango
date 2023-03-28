from django.contrib import admin

from .models import Acessorio, Categoria, Cor, Marca

admin.site.register(Acessorio)
admin.site.register(Categoria)
admin.site.register(Cor)
admin.site.register(Marca)