<template>
  <div class="pagos-container">
    <!-- Botón que abre el calendario -->
   <VBtn color="primary" @click="mostrarCalendario = true">
  {{ formatearFecha(fechaSeleccionada) }}
</VBtn>

<VDialog v-model="mostrarCalendario" max-width="350">
  <VCard>
    <VDatePicker
      v-model="fechaSeleccionada"
      locale="es"
      :show-current="true"
      @update:model-value="filtrarPagos"
    />
    <VCardActions>
      <VBtn text color="primary" @click="mostrarCalendario = false">Cerrar</VBtn>
    </VCardActions>
  </VCard>
</VDialog>


    <!-- Tabla de pagos -->
    <v-table class="ma-4 pa-4">
      <thead>
        <tr>
          <th>ID</th>
          <th>Reserva</th>
          <th>Fecha</th>
          <th>Cantidad</th>
          <th>Método de Pago</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="pago in pagosFiltrados" :key="pago.id">
          <td>{{ pago.id }}</td>
          <td>{{ pago.reserva_id }}</td>
          <td>{{ formatearFecha(pago.fecha) }}</td>
          <td>{{ pago.cantidad }}</td>
          <td>{{ pago.metodoDePago }}</td>
        </tr>
        <tr v-if="pagosFiltrados.length === 0">
          <td colspan="5">No hay pagos para la fecha seleccionada.</td>
        </tr>
      </tbody>
    </v-table>

    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { VBtn, VDatePicker, VCard } from "vuetify/components"
import { getpagos } from "@/api/pago"

const pagos = ref([])
const pagosFiltrados = ref([])
const fechaSeleccionada = ref(new Date())
const mostrarCalendario = ref(false)
const error = ref(null)
const loading = ref(false)


// Formatear fecha a formato legible
const formatearFecha = (fecha) => {
  if (!fecha) return ""
  return new Date(fecha).toLocaleDateString("es-ES", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  })
}

// Filtrar pagos por fecha seleccionada
const filtrarPagos = () => {
  pagosFiltrados.value = pagos.value.filter((pago) => {
    const pagoFecha = new Date(pago.fecha)
    const fechaSel = fechaSeleccionada.value

    return (
      pagoFecha.getUTCFullYear() === fechaSel.getFullYear() &&
      pagoFecha.getUTCMonth() === fechaSel.getMonth() &&
      pagoFecha.getUTCDate() === fechaSel.getDate()
    )
  })
}


// Simulación de carga de pagos desde la API
const cargarPagos = async () => {
 loading.value = true
    error.value = null
    pagos.value = []
    try {
        pagos.value = await getpagos()
    } catch (e) {
        error.value = 'Error al cargar pagos'
    } finally {
        loading.value = false
    }
}

onMounted(() => {
  cargarPagos()
})
</script>

<style scoped>
.pagos-container {
  max-width: 900px;
  margin: auto;
  background-color: #0A1828; /* azul oscuro */
  color: #F9F9F9; /* texto claro */
  padding: 20px;
  border-radius: 12px;
}

/* Botones */
.v-btn {
  background-color: #BFA181 !important; /* dorado */
  color: #0A1828 !important; /* contraste */
  font-weight: bold;
}
.v-btn:hover {
  background-color: #178582 !important; /* turquesa */
  color: #fff !important;
}

/* Tabla */
.v-table thead {
  background-color: #0A1828;
}
.v-table thead th {
  color: #BFA181;
  font-weight: bold;
  text-transform: uppercase;
}
.v-table tbody tr:nth-child(even) {
  background-color: #111e36; /* tono más claro del azul */
}
.v-table tbody td {
  color: #F9F9F9;
}

/* Cantidad */
.v-table tbody td:nth-child(4) {
  font-weight: bold;
  color: #BFA181;
}

/* Mensaje vacío */
.empty-msg {
  text-align: center;
  padding: 16px;
  color: #BFA181;
}
</style>
