<template>
    <div>

        <ul v-if="reservas.length > 0">
            <li v-for="reserva in reservas" :key="reserva.id">
                <router-link :to="`/Reserva/${reserva.id}`"> {{ reserva.id }}</router-link>
            </li>
        </ul>
        

        <p v-if="error" style="color: red">{{ error }}</p>
 <v-btn>Button</v-btn>

    </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import { getReservas } from "../api/reserva.js";

const reservas = ref([])
const loading = ref(false)
const error = ref(null)


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

onMounted(() => {
  cargarreservas()
})

</script>