from django.contrib import admin
from .models import Edificio, Departamento


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_propietario', 'costo', 'numero_cuartos', 'edificio')    
    search_fields = ('nombre_propietario', 'costo', 'numero_cuartos', 'edificio__nombre')
    
class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion', 'ciudad', 'tipo')
    
admin.site.register(Edificio, EdificioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)