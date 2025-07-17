from django.db import models

# Create your models here.
class Usuario(models.Model):
   id = models.IntegerField(primary_key=True)
   nombre = models.CharField(max_length=50)
   mail = models.CharField(max_length=50)
   contraseña = models.CharField(max_length=50)
   fotoDePerfil = models.ImageField

class TipoAlojamiento(models.Model):
   id  = models.IntegerField(primary_key=True)
   descripcion = models.CharField(max_length=50)


class Alojamiento(models.Model):
   id = models.IntegerField(primary_key=True)
   nombre = models.CharField(max_length=50)
   direccion = models.CharField(max_length=50)  
   TipoAlojamiento_id = models.ForeignKey(TipoAlojamiento, on_delete=models.CASCADE)
   
class TipoHabitacion(models.Model):
   id= models.IntegerField(primary_key=True)
   descripcion= models.CharField(max_length=50)

class Habitacion(models.Model):
   id= models.IntegerField(primary_key=True)
   nombre= models.CharField(max_length=50)
   tipoHabitacion_id=models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
   camasSimples= models.IntegerField()
   camasDobles= models.IntegerField()
   bañoPrivado=models.BooleanField()
   cocina =models.BooleanField()
   desayuno=models.BooleanField()
   precio= models.DecimalField(max_digits=10, decimal_places=2)
   alojamiento_id = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)   

class Reserva(models.Model):
   id= models.IntegerField(primary_key=True)
   habitacion_id = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
   cantNoches= models.IntegerField()
   desde= models.DateTimeField()
   hasta= models.DateTimeField()
   checkIn= models.DateTimeField()
   checkOut= models.DateTimeField()
   nombreHuesped= models.CharField(max_length=50)
   identificacion= models.CharField(max_length=50)
   precio= models.DecimalField(max_digits=10, decimal_places=2)
   pagado= models.BooleanField()

class Pago(models.Model):
   id= models.IntegerField(primary_key=True)
   reserva_id = models.ForeignKey(Reserva, on_delete=models.CASCADE)
   fecha= models.DateTimeField()
   cantidad= models.DecimalField(max_digits=10, decimal_places=2)
   metodoDePago = models.CharField(max_length=50)   