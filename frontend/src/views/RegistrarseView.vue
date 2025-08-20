<template>
    <h2>Registrarse</h2>

    <VForm v-if="!mostrarFormularioAlojamiento">
      <label>Nombre de usuario:
        <VTextField v-model="usuario.username" required />
      </label>

      <label>Email:
        <VTextField type="email" v-model="usuario.email" required />
      </label>

      <label>Contraseña:
        <VTextField type="password" v-model="usuario.password" required />
      </label>

      <label>Tipo de cuenta:
        <select v-model="usuario.grupo" required>
          <option value="cliente">Cliente</option>
          <option value="propietario">Propietario</option>
        </select>
      </label>

      <button @click="registrar">Guardar</button>
    </VForm>

    <!-- Formulario de Alojamiento solo si es propietario -->
    <VForm v-else>
      <h3>Crear Alojamiento</h3>

      <label>Nombre del alojamiento:
        <VTextField v-model="alojamiento.nombre" required />
      </label>

        <label>Ubicacion:
        <VTextField v-model="alojamiento.ubicacion" required />
      </label>


      <label>Dirección:
        <VTextField v-model="alojamiento.direccion" required />
      </label>

      <label>Tipo de alojamiento:
  <VTextField v-model="alojamiento.tipoAlojamiento" required />
</label>

      <button @click="guardarAlojamiento">Guardar Alojamiento</button>
    
    </VForm>
</template>


<script setup>
import { ref } from 'vue'
import { registrarUsuario } from '../api/registrarse.js'
import { createAlojamiento } from '../api/alojamiento.js'
import { useRouter } from 'vue-router'
import { VForm, VTextField } from 'vuetify/lib/components/index.js'

const router = useRouter()

const usuario = ref({
  username: '',
  email: '',
  password: '',
  grupo: ''
})

const mostrarFormularioAlojamiento = ref(false)

const alojamiento = ref({
  nombre: '',
  ubicacion:'',
  direccion: '',
  tipoAlojamiento: ''
})



const registrar = async () => {
  try {
     await registrarUsuario(usuario.value)

    if (usuario.value.grupo === 'cliente') {
      router.push('/bienvenida')
    } else if (usuario.value.grupo === 'propietario') {
      mostrarFormularioAlojamiento.value = true
    }
  } catch (err) {
    alert('Error al crear el usuario')
  }
}

const guardarAlojamiento = async () => {
  try {
    await createAlojamiento(alojamiento.value)
    router.push('/bienvenida')
  } catch (error) {
    console.error('Error al guardar el pago:', error.response?.data || error.message)
      console.error('Respuesta completa del error:', error)
      console.table(error.response.data) 
    alert('Error al crear el alojamiento')
  }
}
</script>
