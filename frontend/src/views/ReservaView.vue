<template>
  <div class="reserva-container">
    <p v-if="loading" class="loading-text">Cargando reservas...</p>

    <div v-else-if="reserva" class="card">
      <!-- Vista de solo lectura -->
      <div v-if="!editar">
        <h2 class="card-title">Reserva #{{ reserva.id }}</h2>
        <p><strong>Noches:</strong> {{ reserva.cantNoches }}</p>
        <p><strong>Desde:</strong> {{ reserva.desde }}</p>
        <p><strong>Hasta:</strong> {{ reserva.hasta }}</p>
        <p><strong>Check In:</strong> {{ reserva.checkIn }}</p>
        <p><strong>Check Out:</strong> {{ reserva.checkOut }}</p>
        <p><strong>Huésped:</strong> {{ reserva.nombreHuesped }}</p>
        <p><strong>Identificación:</strong> {{ reserva.identificacion }}</p>
        <p><strong>Precio:</strong> ${{ reserva.precio }}</p>
        <p>
          <strong>Pagado:</strong>
          <span :class="reserva.pagado ? 'pagado' : 'pendiente'">
            {{ reserva.pagado ? 'Sí' : 'No' }}
          </span>
        </p>

        <div class="acciones">
          <button @click="editar = true" class="btn">Editar</button>
          <button @click="eliminarReserva" class="btn danger">Eliminar</button>
          <button @click="pagar = true" class="btn success">Registrar pago</button>
        </div>
      </div>

      <!-- Formulario de edición -->
      <div v-else class="formulario">
        <h2 class="card-title">Editar Reserva</h2>

        <label>Cantidad de noches
          <input v-model="reserva.cantNoches" type="number" />
        </label>

        <label>Fecha de entrada
          <input type="date" v-model="reserva.desde" />
        </label>

        <label>Fecha de salida
          <input type="date" v-model="reserva.hasta" />
        </label>

        <div v-if="auth.grupos.includes('propietario')">
          <label>Nombre huésped
            <input v-model="reserva.nombreHuesped" />
          </label>
          <label>ID huésped
            <input v-model="reserva.identificacion" />
          </label>
          <label>Precio
            <input type="number" v-model="reserva.precio" />
          </label>
          <label>Pagado
            <select v-model="reserva.pagado">
              <option :value="true">Sí</option>
              <option :value="false">No</option>
            </select>
          </label>
          <label>Check in
            <input v-model="reserva.checkIn" type="datetime-local" />
          </label>
          <label>Check out
            <input v-model="reserva.checkOut" type="datetime-local" />
          </label>
        </div>

        <div class="acciones">
          <button @click="editarReserva" class="btn success">Guardar</button>
          <button @click="editar = false" class="btn secondary">Cancelar</button>
        </div>
      </div>
    </div>

    <!-- Formulario de pago -->
    <div v-if="pagar" class="card pago-card">
      <h2 class="card-title">Registrar Pago</h2>
      <label>Método de pago:
        <input v-model="pago.metodoDePago" />
      </label>
      <div class="acciones">
        <button @click="GuardarPago" class="btn success">Guardar</button>
        <button @click="pagar = false" class="btn secondary">Cancelar</button>
      </div>
    </div>

    <!-- Errores -->
    <p v-if="error" class="error-text">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import { getReserva, updateReserva, deleteReserva } from "../api/reserva.js"
import { createpago } from "../api/pago.js"
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

const reserva = ref(null)
const loading = ref(false)
const error = ref(null)
const editar = ref(false)
const pagar = ref(false)

const pago = ref({
  reserva_id: route.params.id,
  fecha: new Date().toISOString().slice(0, 19),
  cantidad: 0,
  metodoDePago: "",
})

const cargarReserva = async () => {
  loading.value = true
  error.value = null
  try {
    reserva.value = await getReserva(route.params.id)
  } catch (e) {
    error.value = 'Error al cargar reserva'
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  cargarReserva()
})

const editarReserva = async () => {
  try {
    await updateReserva(reserva.value.id, reserva.value)
    editar.value = false
  } catch (err) {
    error.value = 'Error al actualizar la reserva'
  }
}

const eliminarReserva = async () => {
  if (confirm('¿Estás segura/o de eliminar esta reserva?')) {
    try {
      await deleteReserva(route.params.id)
      router.push('/Reservas')
    } catch (e) {
      error.value = 'Error al eliminar la reserva'
    }
  }
}

const GuardarPago = async () => {
  pago.value.cantidad = reserva.value.precio
  try {
    await createpago(pago.value)
    pagar.value = false
  } catch (err) {
    error.value = 'Error al guardar la información de pago'
  }
}
</script>

<style scoped>
.reserva-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 15px;
  font-family: 'Poppins', sans-serif;
}

.loading-text {
  text-align: center;
  font-size: 18px;
}

.error-text {
  color: red;
  margin-top: 10px;
  text-align: center;
}

.card {
  background: #f8eee7;
  border: 2px solid #94618e;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
}

.card-title {
  font-size: 22px;
  margin-bottom: 15px;
  color: #49274a;
}

label {
  display: block;
  margin-bottom: 12px;
  font-weight: 500;
}

input, select {
  width: 100%;
  padding: 8px;
  margin-top: 4px;
  border: 1px solid #94618e;
  border-radius: 6px;
}

.acciones {
  margin-top: 15px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn {
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: 0.3s;
}

.btn.success {
  background-color: #94618e;
  color: #f8eee7;
}
.btn.success:hover {
  background-color: #49274a;
}

.btn.danger {
  background-color: #d9534f;
  color: white;
}
.btn.danger:hover {
  background-color: #b52b27;
}

.btn.secondary {
  background-color: #ccc;
  color: #333;
}
.btn.secondary:hover {
  background-color: #999;
}

.pagado {
  color: green;
  font-weight: 600;
}
.pendiente {
  color: red;
  font-weight: 600;
}
</style>
