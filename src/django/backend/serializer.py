from rest_framework import serializers
from .models import Usuario,TipoAlojamiento,Alojamiento,TipoHabitacion,Habitacion,Reserva,Pago

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TipoAlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAlojamiento
        fields = '__all__'

class AlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = '__all__'

class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'

class SimpleAlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = ('nombre','id')



class HabitacionSerializer(serializers.ModelSerializer):
    alojamiento=SimpleAlojamientoSerializer( read_only=True)
    class Meta:
        model = Habitacion
        fields = (
            'id',
            'nombre',
            'tipoHabitacion_id',
            'camasSimples',
            'camasDobles',
            'bañoPrivado',
            'cocina',
            'desayuno',
            'precio',
            'alojamiento'
        )     

class SimpleUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nombre','id')

class SimpleHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ('nombre','id')        

class ReservaSerializer(serializers.ModelSerializer):
    habitacion=SimpleHabitacionSerializer( read_only=True)
    usuario=SimpleUsuarioSerializer( read_only=True)
    class Meta:
        model = Reserva
        fields = (
            'id',
            'habitacion',
            'usuario',
            'cantNoches',
            'desde',
            'hasta',
            'checkIn',
            'checkOut',
            'nombreHuesped',
            'identificacion',
            'precio',
            'pagado'
        )

class SimpleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('nombre','id')        

class PagoSerializer(serializers.ModelSerializer):
    reserva=SimpleReservaSerializer( read_only=True)
    class Meta:
        model = Pago
        fields = (
            'id',
            'reserva',
            'fecha',
            'cantidad',
            'metodoDePago'
        )
