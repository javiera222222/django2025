from django.urls import path

from .views  import AlojamientoList,AlojamientoDetail,HabitacionList,HabitacionDetail,ReservaList,ReservaDetail,PagoList,PagoDetail

urlpatterns = [

    path('api/alojamiento/',AlojamientoList.as_view()),
    path('api/alojamiento/<int:pk>/',AlojamientoDetail.as_view()),
    path('api/habitacion/',HabitacionList.as_view()),
    path('api/habitacion/<int:pk>/',HabitacionDetail.as_view()),
    path('api/reserva/',ReservaList.as_view()),
    path('api/reserva/<int:pk>/',ReservaDetail.as_view()),
    path('api/pago/',PagoList.as_view()),
    path('api/pago/<int:pk>/',PagoDetail.as_view()),]
    
    
    
    