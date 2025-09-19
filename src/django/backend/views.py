from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date
from django.template import Template,Context
from django.template.loader import get_template
from .models import Alojamiento,Habitacion,Reserva,Pago
from .serializer import AlojamientoSerializer,HabitacionSerializer,ReservaSerializer,PagoSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



class AlojamientoList(generics.ListCreateAPIView):
    queryset =Alojamiento.objects.all()
    serializer_class = AlojamientoSerializer
     

class AlojamientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Alojamiento.objects.all()
    serializer_class=AlojamientoSerializer 
      

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


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # si es propietario -> solo reservas de sus alojamientos
        if user.groups.filter(name="propietario").exists():
            return Reserva.objects.filter(
                habitacion__alojamiento_id__user_id=user
            )

        # si es cliente -> mostrar solo reservas que hizo él
        if user.groups.filter(name="cliente").exists():
            # ⚠️ tu modelo Reserva no tiene campo usuario todavía,
            # así que aquí no se puede filtrar por cliente.
            # Si planeás agregarlo, quedaría así:
            return Reserva.objects.filter(usuario=user)


        # si no cumple nada, no devolver nada
        return Reserva.objects.none()

class PagoList(generics.ListCreateAPIView):
    queryset =Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes=(IsAuthenticated,)  

class PagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Pago.objects.all()
    serializer_class=PagoSerializer 
    permission_classes=(IsAuthenticated,)   

   