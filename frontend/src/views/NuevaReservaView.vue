<template>
  <div v-if="habitacion">
    <p>Nombre: {{ habitacion.nombre }}</p>
    <p>Precio: ${{ habitacion.precio }}</p>

    <label>Cantidad de noches:
      <input type="number" v-model.number="reserva.cantNoches" />
    </label>

    <label>Desde:
      <input type="date" v-model="reserva.desde" />
    </label>

    <label>Hasta:
      <input type="date" v-model="reserva.hasta" />
    </label>

    <div v-if="auth.grupos.includes('propietario')" >

    <label>Check-in:
      <input type="datetime-local" v-model="reserva.checkIn" />
    </label>

    <label>Check-out:
      <input type="datetime-local" v-model="reserva.checkOut" />
    </label>

    <label>Nombre huésped:
      <input v-model="reserva.nombreHuesped" />
    </label>

    <label>Identificación:
      <input v-model="reserva.identificacion" />
    </label>

    <label>Precio:
      <input type="number" v-model.number="reserva.precio" />
    </label>

    <label>¿Pagado?
      <input type="checkbox" v-model="reserva.pagado" />
    </label>
    </div>

    <button @click="crearReserva">Guardar reserva</button>

    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { createReserva } from '../api/reserva.js'
import { gethabitacion } from "../api/habitacion.js"

const route = useRoute()
const habitacionId = route.params.id
const error = ref(null)
const habitacion = ref(null)
const loading = ref(false)

const reserva = ref({
  cantNoches: 1,
  desde: '',
  hasta: '',
  checkIn: '',
  checkOut: '',
  nombreHuesped: '',
  identificacion: '',
  precio: 0,
  pagado: false,
  habitacion: habitacionId
})

const crearReserva = async () => {
  try {
    reserva.value.precio = habitacion.value.precio * reserva.value.cantNoches
    await createReserva(reserva.value)
    alert('Reserva creada correctamente')
  } catch (err) {
    console.error('Error al crear reserva:', err)
    error.value = 'Error al crear la reserva'
  }
}

const cargarHabitacion = async () => {
  loading.value = true
  error.value = null
  try {
    habitacion.value = await gethabitacion(habitacionId)
  } catch (e) {
    error.value = 'Error al cargar la habitación'
  } finally {
    loading.value = false
  }
}

onMounted(cargarHabitacion)
</script>
