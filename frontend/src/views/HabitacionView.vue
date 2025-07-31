<template>
  <div> 
    <p v-if="loading">Cargando habitación...</p>

    <div v-else-if="habitacion">
      <div v-if="!editar">
      <p>Nombre: {{ habitacion.nombre }}</p>
      <p>Precio: ${{ habitacion.precio }}</p>
      <p>Tipo: {{ habitacion.tipoHabitacion_id }}</p>
      <p>Camas simples: {{ habitacion.camasSimples }}</p>
      <p>Camas dobles: {{ habitacion.camasDobles }}</p>
      <p>Baño privado: {{ habitacion.bañoPrivado}}</p>
      <p>Cocina: {{ habitacion.cocina}}</p>
      <p>Desayuno: {{ habitacion.desayuno }}</p>
      <p>Alojamiento ID: {{ habitacion.alojamiento_id }}</p>
</div>

  <button v-if="auth.grupos.includes('propietario') && !editar" @click="editar=true">editar</button>
   <div v-if="editar">
      <label>Nombre:
    <input v-model="habitacion.nombre" />
  </label>

  <label>Precio:
    <input v-model.number="habitacion.precio" type="number" />
  </label>

  <label>Tipo:
    <input v-model="habitacion.tipoHabitacion_id" />
  </label>

  <label>Camas simples:
    <input v-model.number="habitacion.camasSimples" type="number" />
  </label>

  <label>Camas dobles:
    <input v-model.number="habitacion.camasDobles" type="number" />
  </label>

  <label>Baño privado:
    <input v-model="habitacion.bañoPrivado" type="checkbox" />
  </label>

  <label>Cocina:
    <input v-model="habitacion.cocina" type="checkbox" />
  </label>

  <label>Desayuno:
    <input v-model="habitacion.desayuno" type="checkbox" />
  </label>

  <label>Alojamiento ID:
    <input v-model="habitacion.alojamiento_id" />
  </label>
    <button  @click="editarHabitacion">guardar edicion</button>
    <button  @click="eliminarHabitacion">Eliminar</button>

</div>

    </div>

    <p v-if="error" style="color: red">{{ error }}</p>


  </div>

 <button v-if="auth.grupos.includes('cliente')"  @click="irAReservaNueva">Reservar esta habitación</button>

   
  

</template>

<script setup>
import { ref,onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { gethabitacion,updatehabitacion,deletehabitacion} from "../api/habitacion.js";
import { useRoute,useRouter } from 'vue-router'

const auth = useAuthStore()
const route = useRoute()
const router = useRouter()
const habitacion = ref(null)
const loading = ref(false)
const error = ref(null)
var editar = ref(false)

const cargarHabitacion = async () => {
    loading.value = true
    error.value = null
    habitacion.value = []
    try {
        habitacion.value = await gethabitacion(route.params.id)
    } catch (e) {
        error.value = 'Error al cargar habitaciones'
    } finally {
        loading.value = false
    }
}

onMounted(() => {
  cargarHabitacion()
})



const editarHabitacion = async () => {
  try {
    await updatehabitacion(habitacion.value.id, habitacion.value)
    console.log('Habitación actualizada')
  } catch (err) {
    console.error('Error al actualizar la habitación:', err)
  }

    editar.value=false;
}




const eliminarHabitacion = async () => {
  if (confirm('¿Estás segura/o de eliminar esta habitación?')) {
    try {
      await deletehabitacion(route.params.id)
      alert('Habitación eliminada correctamente')
      router.push('/Habitaciones') 
    } catch (e) {
      error.value = 'Error al eliminar la habitación'
    }
  }
}

const irAReservaNueva = () => {
  const habitacionId = route.params.id
  router.push(`/habitacion/${habitacionId}/NuevaReserva`)
}


</script>

