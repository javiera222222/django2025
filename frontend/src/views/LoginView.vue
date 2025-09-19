<template>
  <div class="login-wrapper">
    <!-- Columna izquierda con imagen -->
    <div class="login-image"></div>

    <!-- Columna derecha con el formulario -->
    <div class="login-form-container">
      <v-card class="login-card px-8 py-8" max-width="400" elevation="8">
        <v-card-title class="justify-center text-h5 font-weight-bold  title-with-line">
          Iniciar Sesión
        </v-card-title>

        <v-card-text>
          <v-form v-model="formValid" @submit.prevent="handleLogin">
            <!-- Username -->
            <v-text-field
              v-model="username"
              :readonly="loading"
              :rules="[required]"
              label="Nombre de usuario"
              clearable
              prepend-inner-icon="mdi-account"
              class="mb-4 input-violeta"
            ></v-text-field>

            <!-- Password -->
            <v-text-field
              v-model="password"
              :readonly="loading"
              :rules="[required]"
              label="Contraseña"
              clearable
              prepend-inner-icon="mdi-lock"
              type="password"
              class="mb-6 input-violeta"
            ></v-text-field>

            <!-- Botón login -->
            <v-btn
              :disabled="!formValid"
              :loading="loading"
              size="large"
              type="submit"
              variant="elevated"
              block
              class="btn-login"
            >
              Iniciar Sesión
            </v-btn>

            <!-- Texto y botón registrarse -->
            <div class="text-center mt-6">
              <p class="text-secondary">¿No tenés una cuenta creada?</p>
              <v-btn class="btn-register mt-2" to="/Registrarse">
                Registrarse
              </v-btn>
            </div>

            <!-- Mensaje de error -->
            <p v-if="error" class="text-error mt-4 text-center">{{ error }}</p>
          </v-form>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'

const username = ref('')
const password = ref('')
const formValid = ref(false)
const loading = ref(false)
const error = ref(null)

const required = value => !!value || 'Este campo es requerido'

const auth = useAuthStore()

const handleLogin = async () => {
  loading.value = true
  error.value = null
  try {
    await auth.login(username.value, password.value)
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>
 
<style scoped>
/* Fuente general */
* {
  font-family: 'Poppins', sans-serif;
}

/* Wrapper principal: dos columnas */
.login-wrapper {
  display: flex;
  height: 100vh;
  background: #49274a; /* fondo oscuro general */
}

/* Columna izquierda con imagen */
.login-image {
  flex: 1;
  background: url(../../public/hotelinicio.jpg) no-repeat center center;
  background-size: cover;
  display: none; /* oculto en mobile */
}

/* Columna derecha con el form */
.login-form-container {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #49274a; /* mantengo fondo oscuro del contenedor */
}

/* Mostrar imagen solo en pantallas grandes */
@media (min-width: 992px) {
  .login-image {
    display: block;
  }
  .login-form-container {
    flex: 1;
  }
}

/* Card */
.login-card {
  background-color: #f8eee7; /* tarjeta clara */
  color: #49274a; /* texto oscuro */
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
  animation: fadeInUp 0.8s ease;
  padding: 2rem;
}

/* Animación entrada */
@keyframes fadeInUp {
  from {
    transform: translateY(30px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Título con línea */
.title-with-line {
  position: relative;
  color: #49274a; /* mismo color que el resto del texto */
}
.title-with-line::after {
  content: "";
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 50px;
  height: 3px;
  background-color: #49274a;
  border-radius: 3px;
}

/* Inputs */
.input-violeta input {
  color: #49274a; /* texto dentro de inputs */
  background-color: #ffffff; /* fondo claro de input */
}
.input-violeta label {
  color: #49274a; /* label de inputs */
}
.input-violeta input:focus {
  border-bottom: 2px solid #49274a !important;
  box-shadow: 0 2px 6px rgba(73, 39, 74, 0.3);
}

/* Botón login */
.btn-login {
  background-color: #f8eee7 !important; /* mismo color que el card */
  color: #49274a !important; /* texto oscuro */
  font-weight: bold;
  text-transform: uppercase;
  transition: all 0.3s ease;
  border: 2px solid #49274a;
}
.btn-login:hover {
  background-color: #e2d5c7 !important;
  transform: scale(1.02);
}

/* Botón registrarse */
.btn-register {
  background-color: #f4decb !important;
  color: #49274a !important;
  font-weight: bold;
  border-radius: 12px;
  padding: 8px 20px;
  transition: all 0.3s ease;
}
.btn-register:hover {
  background-color: #49274a !important;
  color: #ffffff !important;
  transform: scale(1.05);
}

/* Texto secundario y mensaje de error */
.text-secondary,
.text-error {
  color: #49274a !important; /* mismo color que labels e inputs */
}

</style>