from django.contrib import admin
from backend.models import Alojamiento,Habitacion,Reserva,Pago

admin.site.register(Alojamiento)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Pago)