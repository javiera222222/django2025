<template>
    <div>
        <h2>Bienvenido al Dashboard</h2>
        <button @click="logout">Cerrar sesión</button>

        <br><br><br><br><br>

        <button @click="cargarreservas">Cargar reservas</button>

        <p v-if="loading">Cargando reservas...</p>
        <ul v-else-if="reservas.length > 0">
            <li v-for="reserva in reservas" :key="reserva.id">
                {{ reserva.id }}
            </li>
        </ul>
        <p v-else>No se han cargado reservas aún.</p>

        <p v-if="error" style="color: red">{{ error }}</p>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { getReservas } from "../api/reserva.js";
const auth = useAuthStore()

const reservas = ref([])
const loading = ref(false)
const error = ref(null)

const logout = () => {
    auth.logout()
}

const cargarreservas = async () => {
    loading.value = true
    error.value = null
    reservas.value = []
    try {
        reservas.value = await getReservas()
    } catch (e) {
        error.value = 'Error al cargar reservas'
    } finally {
        loading.value = false
    }
}
</script>