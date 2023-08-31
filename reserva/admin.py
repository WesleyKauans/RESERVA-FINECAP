from django.contrib import admin
from .models import reserva, Stand

@admin.register(reserva)
class ReservaAdmin (admin.ModelAdmin):
    list_display = ['cnpj', 'nome_empresa', 'descricao_empresa', 'quitado']

@admin.register(Stand)
class StandAdmin (admin.ModelAdmin):
    list_display = ['localizacao', 'valor']