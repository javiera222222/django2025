<template>
  <label>Nombre:
    <input v-model="habitacion.nombre" />
  </label>

  <label>Precio:
    <input v-model.number="habitacion.precio" type="number" />
  </label>

  <label>Tipo:
    <input v-model="habitacion.tipoHabitacion_id" />
  </label>

  <label>Camas simples:
    <input v-model.number="habitacion.camasSimples" type="number" />
  </label>

  <label>Camas dobles:
    <input v-model.number="habitacion.camasDobles" type="number" />
  </label>

  <label>Baño privado:
    <input v-model="habitacion.bañoPrivado" type="checkbox" />
  </label>

  <label>Cocina:
    <input v-model="habitacion.cocina" type="checkbox" />
  </label>

  <label>Desayuno:
    <input v-model="habitacion.desayuno" type="checkbox" />
  </label>

  <label>Alojamiento ID:
    <input v-model="habitacion.alojamiento_id" />
  </label>

  <!-- Imagen -->
 

  <label>Imagen de la habitación:
  <input type="file" @change="handleFileChange" />
</label>


  <div v-if="preview">
    <p>Vista previa:</p>
    <img :src="preview" alt="Vista previa" style="max-width: 200px;" />
  </div>

  <button @click="crearHabitacion">Guardar datos</button>

  <p v-if="error" style="color: red">{{ error }}</p>
</template>

<script setup>
import { ref } from 'vue'
import { createhabitacion } from "../api/habitacion.js"
import { useRouter } from 'vue-router'


const archivoImagen = ref(null);
// Cuando el usuario selecciona un archivo
const handleFileChange = (event) => {
  archivoImagen.value = event.target.files[0]; // guardamos el archivo
};
const router = useRouter()
const error = ref(null)
const habitacion = ref({
  nombre: '',
  precio: 0,
  tipoHabitacion_id: 1,
  camasSimples: 0,
  camasDobles: 0,
  bañoPrivado: false,
  cocina: false,
  desayuno: false,
  alojamiento_id: 1,
})
const imagenFile = ref(null)
const preview = ref(null)



const crearHabitacion = async () => {
  try {
    const formData = new FormData()
    for (const key in habitacion.value) {
      formData.append(key, habitacion.value[key])
    }
    if (imagenFile.value) {
      formData.append("imagen", imagenFile.value)
    }

    const habitacionCreada = await createhabitacion(formData, true) 
    router.push(`/habitacion/${habitacionCreada.id}`)
  } catch (err) {
    error.value = 'Error al crear la habitación'
  }
}
</script>

