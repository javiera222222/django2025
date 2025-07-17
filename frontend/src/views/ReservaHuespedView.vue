<template>
    <div>
        <button @click="logout">Cerrar sesión</button>
        <button @click="cargarreserva">Cargar reservas</button>

        <p v-if="loading">Cargando reservas...</p>
        <ul v-else-if="reserva.length > 0">
                {{ reserva.habitacion_id }}
                {{ reserva.cantNoches }}
                {{ reserva.desde }}
                {{ reserva.hasta }}
                {{ reserva.checkIn }}
                {{ reserva.checkOut }}
                {{ reserva.nombreHuesped }}
                {{ reserva.identificacion }}
                {{ reserva.precio }}
                {{ reserva.pagado }}


        </ul>
        <p v-else>No se han cargado reservas aún.</p>

        <p v-if="error" style="color: red">{{ error }}</p>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { getReserva } from "../api/reserva.js";
const auth = useAuthStore()

const reserva = ref([])
const loading = ref(false)
const error = ref(null)

const logout = () => {
    auth.logout()
}

const cargarreserva = async () => {
    loading.value = true
    error.value = null
    reserva.value = []
    try {
        reserva.value = await getReserva()
    } catch (e) {
        error.value = 'Error al cargar reservas'
    } finally {
        loading.value = false
    }
}
</script>