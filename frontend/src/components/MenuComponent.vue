<template>
  <VAppBar>
  <nav v-if="auth.access" class="menu">

    <ul class="navegacion">
      <li ><router-link to="/Calendario" v-if="auth.grupos.includes('propietario')">Calendario</router-link></li>
      <li><router-link to="/Habitaciones">Habitaciones</router-link></li>
      <li><router-link to="/Reservas">Reservas</router-link></li>
      <li><router-link to="/Pagos" v-if="auth.grupos.includes('propietario')">Registro de pagos</router-link></li>
    <li> <button @click="logout">Cerrar sesión</button></li>
    </ul>
  </nav>
</VAppBar>
</template>

<script setup>
import { useAuthStore } from '../stores/auth'
const auth = useAuthStore()

const logout = () => {
    auth.logout()
}

</script>

<style>
.menu {
  background-color: #29a5d7;
  height: 90px;
  width: 100%;
  display: flex;
  align-items: center;

}

ul {
  list-style-type: none;

}

.ingreso {
  margin-left: auto
}

li {
  display: inline-block;
  margin-right: 15px;
  font-size: 20px;

}

a {
  text-decoration: none;
  color: #000;


}
</style>