from django.contrib import admin
from core.models import Empresa, Contrato, Carga, Drone, Droneport, Rota, Viagem

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Contrato)
admin.site.register(Carga)
admin.site.register(Drone)
admin.site.register(Droneport)
admin.site.register(Rota)
admin.site.register(Viagem)