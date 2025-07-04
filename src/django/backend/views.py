from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date
from django.template import Template,Context
from django.template.loader import get_template
from .models import Usuario,TipoAlojamiento,Alojamiento,TipoHabitacion,Habitacion,Reserva,Pago
from .serializer import UsuarioSerializer,TipoAlojamientoSerializer,AlojamientoSerializer,TipoHabitacionSerializer,HabitacionSerializer,ReservaSerializer,PagoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class UsuarioList(generics.ListCreateAPIView):
    queryset =Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes=(IsAuthenticated,)  

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Usuario.objects.all()
    serializer_class=UsuarioSerializer 
    permission_classes=(IsAuthenticated,)   

class TipoAlojamientoList(generics.ListCreateAPIView):
    queryset =TipoAlojamiento.objects.all()
    serializer_class = TipoAlojamientoSerializer
    permission_classes=(IsAuthenticated,)  

class TipoAlojamientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =TipoAlojamiento.objects.all()
    serializer_class=TipoAlojamientoSerializer 
    permission_classes=(IsAuthenticated,)   

class AlojamientoList(generics.ListCreateAPIView):
    queryset =Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer
    permission_classes=(IsAuthenticated,)  

class AlojamientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Alojamiento.objects.all()
    serializer_class=AlojamientoSerializer 
    permission_classes=(IsAuthenticated,)   

class TipoHabitacionList(generics.ListCreateAPIView):
    queryset =TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer
    permission_classes=(IsAuthenticated,)  

class TipoHabitacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =TipoHabitacion.objects.all()
    serializer_class=TipoHabitacionSerializer 
    permission_classes=(IsAuthenticated,)   

class HabitacionList(generics.ListCreateAPIView):
    queryset =Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    permission_classes=(IsAuthenticated,)  

class HabitacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Habitacion.objects.all()
    serializer_class=HabitacionSerializer 
    permission_classes=(IsAuthenticated,)   

class ReservaList(generics.ListCreateAPIView):
    queryset =Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes=(IsAuthenticated,)  

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Reserva.objects.all()
    serializer_class=ReservaSerializer 
    permission_classes=(IsAuthenticated,)   

class PagoList(generics.ListCreateAPIView):
    queryset =Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes=(IsAuthenticated,)  

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Pago.objects.all()
    serializer_class=PagoSerializer 
    permission_classes=(IsAuthenticated,)   

   