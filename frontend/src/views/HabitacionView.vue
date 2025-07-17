<template>
    <div> 
        <button @click="logout">Cerrar sesión</button>
        <button @click="cargarhabitacion">Cargar habitacion</button>
#en esta view se ve toda la informacion de una habitacion especifica
        <p v-if="loading">Cargando habitacion...</p>
        <ul v-else-if="habitacion">
                {{ habitacion.nombre }} 
                {{ habitacion.precio }}
                {{ habitacion.tipoHabitacion_id }} 
                {{ habitacion.camasSimples }} 
                {{ habitacion.camasDobles }} 
                {{ habitacion.bañoPrivado }} 
                {{ habitacion.cocina }}
                {{ habitacion.desayuno }}
                {{ habitacion.alojamiento_id }}
    
        </ul>
        <p v-else>No se ha cargado la habitacion aún.</p>

        <p v-if="error" style="color: red">{{ error }}</p>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { gethabitacion } from "../api/habitacion.js";
const auth = useAuthStore()

const habitacion = ref([])
const loading = ref(false)
const error = ref(null)

const logout = () => {
    auth.logout()
}

const cargarhabitacion = async () => {
    loading.value = true
    error.value = null
    habitacion.value = []
    try {
        habitacion.value = await gethabitacion()
    } catch (e) {
        error.value = 'Error al cargar la habitacion'
    } finally {
        loading.value = false
    }
}
</script>