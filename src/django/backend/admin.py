from django.contrib import admin
from backend.models import TipoAlojamiento,Alojamiento,TipoHabitacion,Habitacion,Reserva,Pago

admin.site.register(TipoAlojamiento)
admin.site.register(Alojamiento)
admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Pago)