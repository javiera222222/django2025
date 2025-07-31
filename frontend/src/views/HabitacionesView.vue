<template>
    <div>
        <p v-if="loading">Cargando habitaciones...</p>
        <ul v-else-if="habitaciones.length > 0">
            <li v-for="habitacion in habitaciones" :key="habitacion.id">
            <router-link :to="`/Habitacion/${habitacion.id}`">{{ habitacion.nombre }}  {{ habitacion.precio }}</router-link>
                
            </li>
        </ul>
        <p v-else>No se han cargado habitaciones aún.</p>

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