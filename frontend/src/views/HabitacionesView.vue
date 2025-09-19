<template>
  <div class="habitaciones-container">
    <p v-if="loading" class="loading-text">Cargando habitaciones...</p>

    <v-row dense>
      <v-col
        v-for="habitacion in habitaciones"
        :key="habitacion.id"
        cols="12"
        sm="6"
        md="4"
      >
        <v-card class="habitacion-card" outlined>
          <!-- Nombre y tipo -->
          <v-card-title class="habitacion-nombre">
            {{ habitacion.nombre }}
            <span class="habitacion-tipo" v-if="habitacion.tipoHabitacion">- {{ habitacion.tipoHabitacion }}</span>
          </v-card-title>

          <!-- Info rápida -->
          <v-card-text class="habitacion-info">
            <!-- Icono de habitación / camas -->


  <div class="habitacion-camas">
  <img src="../../public/camas.png" alt="cama Logo" class="logo-img" />

  <span v-if="habitacion.camasSimples > 0">
    {{ habitacion.camasSimples }} cama{{ habitacion.camasSimples > 1 ? 's' : '' }} simple{{ habitacion.camasSimples > 1 ? 's' : '' }}
  </span>

  <span v-if="habitacion.camasDobles > 0">
    {{ habitacion.camasSimples > 0 ? ' & ' : '' }}
    {{ habitacion.camasDobles }} cama{{ habitacion.camasDobles > 1 ? 's' : '' }} doble{{ habitacion.camasDobles > 1 ? 's' : '' }}
  </span>
</div>


<!-- Icono de baño -->
<div>
  <img src="../../public/ducha.png" alt="baño Logo" class="logo-img" />
  {{ habitacion.bañoPrivado ? 'Baño privado' : 'Baño compartido' }}
</div>

<!-- Icono de cocina -->
<div v-if="habitacion.cocina">
  <img src="../../public/frito.png" alt="cocina Logo" class="logo-img" />
  Cocina disponible
</div>

<!-- Icono de desayuno -->
<div v-if="habitacion.desayuno">
  <img src="../../public/desayuno.png" alt="desayuno Logo" class="logo-img" />
  Desayuno incluido
</div>

<!-- Icono de ubicación -->
<div>
  <img src="../../public/mapa.png" alt="ubicacion Logo" class="logo-img" />
  {{ habitacion.alojamiento?.direccion }} - {{ habitacion.alojamiento?.ubicacion }}
</div>

          </v-card-text>

          <!-- Precio -->
          <v-card-subtitle class="habitacion-precio">
            ${{ habitacion.precio }}
          </v-card-subtitle>

          <!-- Botón ver detalle -->
          <v-card-actions>
            <router-link :to="`/Habitacion/${habitacion.id}`">
              <v-btn class="detalle-btn" text>Ver detalle</v-btn>
            </router-link>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <p v-if="error" class="error-text">{{ error }}</p>

    <router-link
      v-if="auth.grupos.includes('propietario')"
      to="/NuevaHabitacion"
      class="nueva-habitacion-btn"
    >
      Nueva Habitación
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useAuthStore } from "../stores/auth"
import { gethabitaciones } from "../api/habitacion.js"
import { getAlojamiento } from "@/api/alojamiento"

const auth = useAuthStore()
const habitaciones = ref([])
const loading = ref(false)
const error = ref(null)

const cargarhabitaciones = async () => {
  loading.value = true
  error.value = null
  habitaciones.value = []
  try {
    habitaciones.value = await gethabitaciones()
    for (let h of habitaciones.value) {
      try {
        const alojamiento = await getAlojamiento(h.alojamiento_id)
        h.alojamiento = alojamiento
      } catch (err) {
        console.error("Error cargando alojamiento", err)
      }
    }
  } catch (e) {
    error.value = "Error al cargar habitaciones"
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  cargarhabitaciones()
})
</script>

<style scoped>
.habitaciones-container {
  padding: 20px;
  background-color: #f8eee7;
  min-height: 100vh;
}

/* Loading y error */
.loading-text {
  color: #94618e;
  font-weight: bold;
  margin-bottom: 20px;
}
.error-text {
  color: red;
  font-weight: bold;
  margin-top: 20px;
}

/* Tarjetas de habitación */
.habitacion-card {
  background-color: #f4decb;
  border-radius: 12px;
  padding: 16px;
  transition: transform 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}
.habitacion-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

/* Nombre y tipo */
.habitacion-nombre {
  font-size: 22px;
  font-weight: 700;
  color: #49274a;
  display: flex;
  justify-content: space-between;
}
.habitacion-tipo {
  font-size: 16px;
  font-weight: 500;
  color: #49274a;
}

/* Info rápida */
.habitacion-info {
  font-size: 16px;
  color: #49274a;
  margin: 12px 0;
  line-height: 1.4;
}
.habitacion-info div {
  display: flex;
  align-items: center;
  gap: 6px; /* separación entre icono y texto */
  margin-bottom: 6px;
}


/* Precio */
.habitacion-precio {
  font-size: 18px;
  font-weight: 600;
  color: #49274a;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 12px;
}

/* Botón ver detalle */
.detalle-btn {
  background-color: #49274a;
  color: #f8eee7 !important;
  font-weight: bold;
  border-radius: 8px;
  padding: 6px 16px;
}
.detalle-btn:hover {
  background-color: #94618e;
}

/* Botón nueva habitación */
.nueva-habitacion-btn {
  display: inline-block;
  margin-top: 25px;
  background-color: #49274a;
  color: #f8eee7;
  font-weight: bold;
  padding: 10px 20px;
  border-radius: 8px;
  text-decoration: none;
  transition: background-color 0.3s;
}
.nueva-habitacion-btn:hover {
  background-color: #94618e;
}
img{
  height: 25px;
}
</style>
