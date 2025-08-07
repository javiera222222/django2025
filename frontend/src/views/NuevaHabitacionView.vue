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
    <button  @click="crearHabitacion">guardar datos</button>
   


    <p v-if="error" style="color: red">{{ error }}</p>

</template>

<script setup>
import { ref} from 'vue'
import { createhabitacion} from "../api/habitacion.js";
import { useRouter } from 'vue-router'


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


const crearHabitacion = async () => {
  try {
 const habitacionCreada = await createhabitacion(habitacion.value)
  router.push(`/habitacion/${habitacionCreada.id}`)
  } catch (err) {
    error.value = 'Error al crear la habitacion'
  }
}


</script>

