<template>
    <div>
        <button @click="logout">Cerrar sesión</button>
        <button @click="cargarhabitaciones">Cargar habitaciones</button>
#en esta view se ve la lista de habitaciones
        <p v-if="loading">Cargando habitaciones...</p>
        <ul v-else-if="habitaciones.length > 0">
            <li v-for="habitacion in habitaciones" :key="habitacion.id">
                {{ habitacion.nombre }}  {{ habitacion.precio }}
            </li>
        </ul>
        <p v-else>No se han cargado habitaciones aún.</p>

        <p v-if="error" style="color: red">{{ error }}</p>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { gethabitaciones } from "../api/habitacion.js";
const auth = useAuthStore()

const habitaciones = ref([])
const loading = ref(false)
const error = ref(null)

const logout = () => {
    auth.logout()
}

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
</script>