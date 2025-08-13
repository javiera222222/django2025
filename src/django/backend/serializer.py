from rest_framework import serializers
from .models import Alojamiento,Habitacion,Reserva,Pago


class AlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = '__all__'
       

class SimpleAlojamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alojamiento
        fields = ('nombre','id')



class HabitacionSerializer(serializers.ModelSerializer):
    alojamiento=AlojamientoSerializer( read_only=True)
    class Meta:
        model = Habitacion
        fields ='__all__'   



class SimpleHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ('nombre','id')        

class ReservaSerializer(serializers.ModelSerializer):
    habitacion = serializers.PrimaryKeyRelatedField(queryset=Habitacion.objects.all())
   
    class Meta:
        model = Reserva
        fields = '__all__'
class SimpleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('nombre','id')        

class PagoSerializer(serializers.ModelSerializer):
    reserva=SimpleReservaSerializer( read_only=True)
    class Meta:
        model = Pago
        fields = '__all__'