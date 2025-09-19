<template>
  <div class="register-container">
    <!-- Columna izquierda: formulario -->
    <div class="form-section">
      <v-card class="register-card pa-6" elevation="6">
        <h2 class="text-center mb-6">Registrarse</h2>

        <!-- Formulario de registro -->
        <VForm v-if="!mostrarFormularioAlojamiento">
          <VTextField
            v-model="usuario.username"
            label="Nombre de usuario"
            required
          />

          <VTextField
            type="email"
            v-model="usuario.email"
            label="Email"
            required
          />

          <VTextField
            type="password"
            v-model="usuario.password"
            label="Contraseña"
            required
          />

          <VSelect
            v-model="usuario.grupo"
            :items="[
              { title: 'Cliente', value: 'cliente' },
              { title: 'Propietario', value: 'propietario' }
            ]"
            label="Tipo de cuenta"
            required
          />

          <v-btn
            class="w-100 mt-4 custom-btn"
            @click.prevent="registrar"
          >
            Guardar
          </v-btn>

          <p class="text-center mt-4">
            ¿Ya tenés una cuenta?
            <RouterLink to="/login" class="link">Iniciar sesión</RouterLink>
          </p>
        </VForm>

        <!-- Formulario de Alojamiento (solo propietarios) -->
        <VForm v-else>
          <h3 class="text-center mb-4">Crear Alojamiento</h3>

          <VTextField
            v-model="alojamiento.nombre"
            label="Nombre del alojamiento"
            required
          />

          <VTextField
            v-model="alojamiento.ubicacion"
            label="Ubicación"
            required
          />

          <VTextField
            v-model="alojamiento.direccion"
            label="Dirección"
            required
          />

          <VTextField
            v-model="alojamiento.tipoAlojamiento"
            label="Tipo de alojamiento"
            required
          />

          <v-btn
            class="w-100 mt-4 custom-btn"
            @click.prevent="guardarAlojamiento"
          >
            Guardar Alojamiento
          </v-btn>
        </VForm>
      </v-card>
    </div>

    <!-- Columna derecha: imagen -->
    <div class="image-section"></div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { registrarUsuario } from "../api/registrarse.js";
import { createAlojamiento } from "../api/alojamiento.js";
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()

import {
  VForm,
  VTextField,
  VSelect,
  VBtn,
  VCard,
} from "vuetify/lib/components/index.js";

const usuario = ref({
  username: "",
  email: "",
  password: "",
  grupo: "",
});

const mostrarFormularioAlojamiento = ref(false);

const alojamiento = ref({
  nombre: "",
  ubicacion: "",
  direccion: "",
  tipoAlojamiento: "",
  
});

const registrar = async () => {
  try {
    await registrarUsuario(usuario.value);

    if (usuario.value.grupo === "cliente") {
      await auth.login(usuario.value.username, usuario.value.password) // 👈 lo manda al inicio como usuario ya registrado
    } else if (usuario.value.grupo === "propietario") {
      mostrarFormularioAlojamiento.value = true;
    }
  } catch (err) {
    alert("Error al crear el usuario");
  }
};

const guardarAlojamiento = async () => {
  try {
     const datos = {
      ...alojamiento.value,   // copia todos los campos del alojamiento
      user_id: usuario.value.id // agrega el user_id
    };
    await createAlojamiento(datos);
    await auth.login(usuario.value.username, usuario.value.password); // 👈 también lo manda al inicio
  } catch (error) {
    console.error("Error al guardar alojamiento:", error);
    alert("Error al crear el alojamiento");
  }
};
</script>

<style scoped>
.register-container {
  display: flex;
  height: 100vh;
}

/* Izquierda: formulario */
.form-section {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #49274a; /* violeta oscuro */
}

.register-card {
  width: 90%;
  max-width: 400px;
  background-color: #f8eee7; /* color claro */
  color: #49274a;
}

/* Botón personalizado */
.custom-btn {
  background-color: #94618e !important; /* violeta medio */
  color: #f8eee7 !important; /* texto claro */
  font-weight: bold;
  border-radius: 8px;
}

.custom-btn:hover {
  background-color: #49274a !important; /* más oscuro al pasar */
}

/* Labels más legibles */
.v-input label {
  font-size: 1rem;
  font-weight: 600;
  color: #49274a !important;
}

/* Link de inicio de sesión */
.link {
  color: #94618e;
  font-weight: bold;
  text-decoration: none;
}
.link:hover {
  text-decoration: underline;
}

/* Derecha: imagen */
.image-section {
  flex: 1;
  background: url(../../public/hotelregistrarse.jpg) no-repeat center center;
  background-size: cover;
}

/* Responsive: ocultar imagen en pantallas chicas */
@media (max-width: 768px) {
  .image-section {
    display: none;
  }
}
</style>
