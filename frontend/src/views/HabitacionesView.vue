<template>
    <div>
        <p v-if="loading">Cargando habitaciones...</p>

<v-list
  :lines="false"
  density="compact"
  nav
>
  <v-list-item
    v-for="habitacion in habitaciones"
    :key="habitacion.id"
    :to="`/Habitacion/${habitacion.id}`"
    color="primary"
  >
    <v-list-item-title>
      {{ habitacion.nombre }}
    </v-list-item-title>
    <v-list-item-subtitle>
      ${{ habitacion.precio }} - {{ habitacion.alojamiento_id.direccion }}
    </v-list-item-subtitle>
  </v-list-item>
</v-list>


        <p v-if="error" style="color: red">{{ error }}</p>

    </div>
  
    <router-link v-if="auth.grupos.includes('propietario')"  to="/NuevaHabitacion">nueva habitacion</router-link>
   
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { gethabitaciones } from "../api/habitacion.js";


const auth = useAuthStore()
const habitaciones = ref([])
const loading = ref(false)
const error = ref(null)




const cargarhabitaciones = async () => {
    loading.value = true
    error.value = null
    habitaciones.value = []
    try {
        habitaciones.value = await gethabitaciones()
    } catch (e) {
        error.value = 'Error al cargar habitaciones'
    } finally {
        loading.value = false
    }
}
onMounted(() => {
  cargarhabitaciones()
})


</script>