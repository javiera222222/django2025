<template>
    <div>
 
        <p v-if="loading">Cargando pago...</p>
        <ul v-else-if="pagos.length > 0">
            <li v-for="pago in pagos" :key="pago.id">
                {{ pago.id }} 
                {{ pago.reserva_id }}
                {{ pago.fecha }} 
                {{ pago.cantidad }} 
                {{ pago.metodoDePago }} 
            </li>  
        </ul>
        <p v-else>No se ha cargado la pago aún.</p>

        <p v-if="error" style="color: red">{{ error }}</p>

    </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import { getpago } from "../api/pago.js";

const pagos = ref([])
const loading = ref(false)
const error = ref(null)

const cargarPago = async () => {
    loading.value = true
    error.value = null
    pagos.value = []
    try {
        pagos.value = await getpago()
    } catch (e) {
        error.value = 'Error al cargar el pago'
    } finally {
        loading.value = false
    }
}

onMounted(() => {
  cargarPago()
})
</script>