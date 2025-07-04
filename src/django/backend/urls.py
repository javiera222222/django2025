from django.urls import path
from .views  import UsuarioList,UsuarioDetail,TipoAlojamientoList,TipoAlojamientoDetail,AlojamientoList,AlojamientoDetail,HabitacionList,HabitacionDetail,TipoHabitacionList,TipoHabitacionDetail,ReservaList,ReservaDetail,PagoList,PagoDetail

urlpatterns = [
    path('api/usuario/',UsuarioList.as_view()),
    path('api/usuario/<int:pk>/',UsuarioDetail.as_view()),
    path('api/TipoAlojamiento/',TipoAlojamientoList.as_view()),
    path('api/TipoAlojamiento/<int:pk>/',TipoAlojamientoDetail.as_view()),
    path('api/alojamiento/',AlojamientoList.as_view()),
    path('api/alojamiento/<int:pk>/',AlojamientoDetail.as_view()),
    path('api/TipoHabitacion/',TipoHabitacionList.as_view()),
    path('api/TipoHabitacion/<int:pk>/',TipoHabitacionDetail.as_view()),
    path('api/habitacion/',HabitacionList.as_view()),
    path('api/habitacion/<int:pk>/',HabitacionDetail.as_view()),
    path('api/reserva/',ReservaList.as_view()),
    path('api/reserva/<int:pk>/',ReservaDetail.as_view()),
    path('api/pago/',PagoList.as_view()),
    path('api/pago/<int:pk>/',PagoDetail.as_view()),]
    
    
    
    
    
    
    