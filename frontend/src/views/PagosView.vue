<template>
    <div>
        <button @click="logout">Cerrar sesión</button>
        <button @click="cargarpago">Cargar pago</button>
#en esta view se ve toda la informacion de una pago especifica
        <p v-if="loading">Cargando pago...</p>
        <ul v-else-if="pago.length > 0">
                {{ pago.id }} 
                {{ pago.reserva_id }}
                {{ pago.fecha }} 
                {{ pago.cantidad }} 
                {{ pago.metodoDePago }} 
                
        </ul>
        <p v-else>No se ha cargado la pago aún.</p>

        <p v-if="error" style="color: red">{{ error }}</p>

    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { getpago } from "../api/pago.js";
const auth = useAuthStore()

const pago = ref([])
const loading = ref(false)
const error = ref(null)

const logout = () => {
    auth.logout()
}

const cargarpago = async () => {
    loading.value = true
    error.value = null
    pago.value = []
    try {
        pago.value = await getpago()
    } catch (e) {
        error.value = 'Error al cargar el pago'
    } finally {
        loading.value = false
    }
}
</script>