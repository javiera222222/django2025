<template>
  <div> 
    <button @click="logout">Cerrar sesión</button>
    <button @click="cargarHabitacion">Cargar habitación</button>

    <p v-if="loading">Cargando habitación...</p>

    
      <p><strong>Nombre:</strong> {{ habitacion.nombre }}</p>
      <p><strong>Precio:</strong> ${{ habitacion.precio }}</p>
      <p><strong>Tipo:</strong> {{ habitacion.tipoHabitacion_id }}</p>
      <p><strong>Camas simples:</strong> {{ habitacion.camasSimples }}</p>
      <p><strong>Camas dobles:</strong> {{ habitacion.camasDobles }}</p>
      <p><strong>Baño privado:</strong> {{ habitacion.bañoPrivado}}</p>
      <p><strong>Cocina:</strong> {{ habitacion.cocina}}</p>
      <p><strong>Desayuno:</strong> {{ habitacion.desayuno }}</p>
      <p><strong>Alojamiento ID:</strong> {{ habitacion.alojamiento_id }}</p>

   

    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { gethabitacion} from "../api/habitacion.js";
const auth = useAuthStore()

const habitaciones = ref([])
const loading = ref(false)
const error = ref(null)

const logout = () => {
    auth.logout()
}

const cargarHabitacion = async () => {
    loading.value = true
    error.value = null
    habitaciones.value = []
    try {
        habitaciones.value = await gethabitacion()
    } catch (e) {
        error.value = 'Error al cargar habitaciones'
    } finally {
        loading.value = false
    }
}
</script>