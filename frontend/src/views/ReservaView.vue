<template>
    <div>
        <p v-if="loading">Cargando reservas...</p>
        <div v-else-if="reserva">
           <div v-if="!editar">
                {{ reserva.reserva_id }}
                {{ reserva.cantNoches }}
                {{ reserva.desde }}
                {{ reserva.hasta }}
                {{ reserva.checkIn }}
                {{ reserva.checkOut }}
                {{ reserva.nombreHuesped }}
                {{ reserva.identificacion }}
                {{ reserva.precio }}
                {{ reserva.pagado }}
            </div>
          <button v-if="!editar" @click="editar=true">editar</button>
   <div v-if="editar">

            <label>Cantidad de noches:
             <input v-model="reserva.cantNoches" />
           </label>
            <label>Fecha de entrada
             <input  type="date" v-model="reserva.desde " />
           </label>
            <label>Fecha de salida
             <input type="date" v-model="reserva.hasta" />
           </label>

            <div v-if="auth.grupos.includes('propietario')">

            <label>Nombre huesped extra
             <input v-model="reserva.nombreHuesped" />
           </label>
            <label>Id huesped
             <input v-model="reserva.identificacion" />
           </label>
            <label>Precio
             <input v-model="reserva.precio" />
           </label>
            <label>Pagado
             <input v-model="reserva.pagado" />
           </label>
           <label>Check in
             <input v-model="reserva.checkIn" />
           </label>
            <label>Check out
             <input v-model="reserva.checkOut" />
           </label>
          </div>
         <button  @click="editarReserva">guardar edicion</button>
         <button  @click="eliminarReserva">Eliminar</button>
          </div>

 </div>
<div>
    <p v-if="error" style="color: red">{{ error }}</p>

    
  </div>

 

        

    </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { getReserva,updateReserva,deleteReserva } from "../api/reserva.js";
import { useRoute,useRouter } from 'vue-router'


const router = useRouter()
const route = useRoute()
const auth = useAuthStore()
const reserva = ref(null)
const loading = ref(false)
const error = ref(null)
var editar = ref(null)



const cargarReserva = async () => {
    loading.value = true
    error.value = null
    reserva.value = []
    try {
        reserva.value = await getReserva(route.params.id)
    } catch (e) {
        error.value = 'Error al cargar reservas'
    } finally {
        loading.value = false
    }
}

onMounted(() => {
  cargarReserva()
})
const editarReserva = async () => {
  try {
    await updateReserva(reserva.value.id, reserva.value)
    console.log('reserva actualizada')
  } catch (err) {
    console.error('Error al actualizar la reserva:', err)
  }

  editar.value=false;
}

const eliminarReserva = async () => {
  if (confirm('¿Estás segura/o de eliminar esta habitación?')) {
    try {
      await deleteReserva(route.params.id)
      alert('Habitación eliminada correctamente')
      router.push('/Habitaciones') // redirige a la lista
    } catch (e) {
      error.value = 'Error al eliminar la habitación'
    }
  }
}
</script>