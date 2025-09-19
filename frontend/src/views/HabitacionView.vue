<template>
  <div class="habitacion-detalle">
    <p v-if="loading" class="loading-text">Cargando habitación...</p>

    <div v-else-if="habitacion" class="habitacion-layout">
      <!-- Columna izquierda: info -->
      <div class="habitacion-info">
        <!-- Título -->
        <h1 class="habitacion-nombre">{{ habitacion.nombre }}</h1>

        <!-- Precio y tipo -->
        <p class="habitacion-precio"> ${{ habitacion.precio }}</p>
        <p class="habitacion-tipo icono-texto">
          <img src="../../public/estrella.png" alt="tipo Logo" class="logo-img" />
          <span>{{ habitacion.tipoHabitacion }}</span>
        </p>

        <!-- Características -->
        <div class="habitacion-caracteristicas">
          <div v-if="habitacion.camasSimples > 0" class="icono-texto">
            <img src="../../public/camas.png" alt="Camas simples" class="logo-img"/>
            <span>
              {{ habitacion.camasSimples }}
              cama{{ habitacion.camasSimples > 1 ? 's' : '' }}
              simple{{ habitacion.camasSimples > 1 ? 's' : '' }}
            </span>
          </div>

          <div v-if="habitacion.camasDobles > 0" class="icono-texto">
            <img src="../../public/camas.png" alt="Camas dobles" class="logo-img"/>
            <span>
              {{ habitacion.camasDobles }}
              cama{{ habitacion.camasDobles > 1 ? 's' : '' }}
              doble{{ habitacion.camasDobles > 1 ? 's' : '' }}
            </span>
          </div>

          <div class="icono-texto">
            <img src="../../public/ducha.png" alt="Baño privado" class="logo-img" />
            <span>{{ habitacion.bañoPrivado ? "Baño privado" : "Baño compartido" }}</span>
          </div>

          <div v-if="habitacion.cocina" class="icono-texto">
            <img src="/icons/frito.svg" alt="Cocina" class="logo-img"/>
            <span>Cocina disponible</span>
          </div>

          <div v-if="habitacion.desayuno" class="icono-texto">
            <img src="/icons/desayuno.svg" alt="Desayuno" class="logo-img"/>
            <span>Desayuno incluido</span>
          </div>
        </div>

        <!-- Info Alojamiento -->
        <div v-if="alojamiento" class="alojamiento-info">
          <h2>Sobre el alojamiento</h2>
          <p><strong>{{ alojamiento.nombre }}</strong></p>
          <p class="icono-texto">
            <img src="../../public/globo-terraqueo.png" alt="ubicacion Logo" class="logo-img" />
            <span>{{ alojamiento.ubicacion }}</span>
          </p>
          <p class="icono-texto">
            <img src="../../public/mapa.png" alt="direccion Logo" class="logo-img"/>
            <span>{{ alojamiento.direccion }}</span>
          </p>
          <p class="icono-texto">
            <img src="../../public/5-estrellas.png" alt="tipo alojamiento Logo" class="logo-img"/>
            <span>{{ alojamiento.tipoAlojamiento }}</span>
          </p>
        </div>

        <!-- Botones -->
        <div class="acciones">
          <button v-if="auth.grupos.includes('propietario')" @click="activarEdicion" class="icono-texto">
            <img src="../../public/lapiz-3d.png" alt="editar logo" class="logo-img"/>
            <span>Editar</span>
          </button>
          <button @click="irAReservaNueva" class="reservar-btn">
            Reservar esta habitación
          </button>
        </div>
      </div>

      <!-- Columna derecha: foto única -->
      <div class="habitacion-foto">
        <img
          v-if="habitacion.imagen"
          :src="habitacion.imagen"
          alt="Foto habitación"
        />
      </div>
    </div>

    <!-- Formulario edición -->
    <div v-if="editar" class="editar-form">
      <label>Nombre: <input v-model="habitacion.nombre" /></label>
      <label>Precio: <input v-model.number="habitacion.precio" type="number" /></label>
      <label>Tipo: <input v-model="habitacion.tipoHabitacion" /></label>
      <label>Camas simples: <input v-model.number="habitacion.camasSimples" type="number" /></label>
      <label>Camas dobles: <input v-model.number="habitacion.camasDobles" type="number" /></label>
      <label>Baño privado: <input v-model="habitacion.bañoPrivado" type="checkbox" /></label>
      <label>Cocina: <input v-model="habitacion.cocina" type="checkbox" /></label>
      <label>Desayuno: <input v-model="habitacion.desayuno" type="checkbox" /></label>
      <label>Alojamiento ID: <input v-model="habitacion.alojamiento_id" /></label>

      <div class="acciones">
        <button @click="editarHabitacion" class="icono-texto">
          <img src="../../public/marcador.png" alt="guardar Logo" class="logo-img"/>
          <span>Guardar</span>
        </button>
        <button @click="eliminarHabitacion" class="eliminar-btn icono-texto">
          <img src="../../public/eliminar.png" alt="eliminar Logo" class="logo-img"/>
          <span>Eliminar</span>
        </button>
      </div>
    </div>

    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>


<script setup>
import { ref, onMounted, nextTick } from "vue";
import { useAuthStore } from "../stores/auth";
import { gethabitacion, updatehabitacion, deletehabitacion } from "../api/habitacion.js";
import { useRoute, useRouter } from "vue-router";
import { getAlojamiento } from "../api/alojamiento.js";


const auth = useAuthStore();
const route = useRoute();
const router = useRouter();

const habitacion = ref(null);
const alojamiento = ref(null);
const loading = ref(false);
const error = ref(null);
const editar = ref(false);



const cargarHabitacion = async () => {
  loading.value = true;
  error.value = null;
  try {
    const data = await gethabitacion(route.params.id);
    habitacion.value = data;

    // Traer alojamiento
    alojamiento.value = await getAlojamiento(data.alojamiento_id);

    // Construir rutas de fotos desde /public/habitaciones/<id>.jpg
    
  } catch (e) {
    error.value = "Error al cargar habitación";
  } finally {
    loading.value = false;
  }
};

onMounted(cargarHabitacion);


const activarEdicion = async () => {
  editar.value = true;
  await nextTick(); // esperar a que se renderice el formulario
  const formEl = document.querySelector(".editar-form");
  if (formEl) {
    formEl.scrollIntoView({ behavior: "smooth", block: "start" });
  }
};

const editarHabitacion = async () => {
  try {
    await updatehabitacion(habitacion.value.id, habitacion.value);
    editar.value = false;
  } catch (e) {
    error.value = "Error al actualizar la habitación";
  }
};

const eliminarHabitacion = async () => {
  if (!confirm("¿Estás segura/o de eliminar esta habitación?")) return;
  try {
    await deletehabitacion(route.params.id);
    router.push("/Habitaciones");
  } catch (e) {
    error.value = "Error al eliminar la habitación";
  }
};

const irAReservaNueva = () => {
  router.push(`/habitacion/${route.params.id}/NuevaReserva`);
};
</script>


<style scoped>
.habitacion-detalle {
  padding: 30px;
  background-color: #f8eee7;
}

.habitacion-layout {
  display: flex;
  gap: 40px;
  align-items: flex-start;
}

.habitacion-info {
  flex: 1;
}

.habitacion-foto{
  flex: 1;
  display: grid;
  grid-template-columns: 1fr;
  gap: 15px;
}

.habitacion-foto img {
  width: 100%;
  border-radius: 12px;
  object-fit: cover;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.habitacion-nombre {
  font-size: 32px;
  font-weight: 700;
  color: #49274a;
}

.habitacion-precio,
.habitacion-tipo {
  font-size: 20px;
  font-weight: 600;
  color: #94618e;
}

.habitacion-caracteristicas div {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 6px 0;
  font-size: 16px;
  color: #49274a;
}

.logo-img {
  width: 22px;
  height: 22px;
}

.alojamiento-info {
  margin-top: 20px;
  background: #f4decb;
  padding: 15px;
  border-radius: 10px;
}


.habitacion-layout {
  display: flex;
  gap: 40px;
  align-items: flex-start;
}

/* --- Responsive --- */
@media (max-width: 768px) {
  .habitacion-layout {
    flex-direction: column; /* texto arriba, fotos abajo */
    gap: 20px;
  }

  .habitacion-fotos {
    grid-template-columns: 1fr 1fr; /* fotos en 2 columnas */
  }

  .habitacion-nombre {
    font-size: 26px;
  }

  .habitacion-precio,
  .habitacion-tipo {
    font-size: 18px;
  }
  .icono-texto {
  display: flex;
  align-items: center;
  gap: 8px;
}

.icono-texto img {
  width: 22px;
  height: 22px;
}

}

/* Inputs bonitos */
/* Inputs más compactos */
/* --- Inputs estilizados --- */
/* --- Inputs estilizados con paleta --- */
/* Formulario en grilla */
.editar-form {
  margin-top: 20px;
  padding: 20px;
  background: #f8eee7;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(73, 39, 74, 0.2);
  animation: fadeInUp 0.4s ease;
  
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); /* se adaptan */
  gap: 16px 24px; /* espacio entre inputs */
}

/* Cada label ocupa su celda en la grilla */
.editar-form label {
  display: flex;
  flex-direction: column;
  font-weight: 600;
  color: #49274a;
  font-size: 13px;
}

/* Inputs compactos (los que ya tenías) */
.editar-form input[type="text"],
.editar-form input[type="number"],
.editar-form input[type="checkbox"] {
  margin-top: 4px;
  padding: 6px 8px;
  border: 1px solid #94618e;
  border-radius: 6px;
  font-size: 13px;
  max-width: 100%;     /* ahora se ajustan al ancho de la celda */
  background: #f4decb;
  color: #49274a;
  transition: all 0.25s ease;
}



/* Botones generales */
.acciones button {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.3s, transform 0.1s;
}

.acciones button img {
  width: 20px;
  height: 20px;
}

/* Botón editar */
.acciones button:first-child {
  background: #94618e;
  color: #fff;
}

.acciones button:first-child:hover {
  background: #49274a;
  transform: scale(1.05);
}

/* Botón reservar */
.reservar-btn {
  background: #49274a;
  color: #f8eee7;
}

.reservar-btn:hover {
  background: #94618e;
  transform: scale(1.05);
}

/* Botón eliminar */
.eliminar-btn {
  background: #d9534f;
  color: #fff;
}

.eliminar-btn:hover {
  background: #c9302c;
  transform: scale(1.05);
}

</style>

