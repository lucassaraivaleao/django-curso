from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from modulos.models import Modulo


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico')
