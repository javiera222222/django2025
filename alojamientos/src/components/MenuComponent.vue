<template>
  <nav class="menu">



    <ul class="navegacion">
      <li><router-link to="/Calendario">Calendario</router-link></li>
      <li><router-link to="/Habitaciones">Habitaciones</router-link></li>
      <li><router-link to="/Reservas">Reservas</router-link></li>
      <li><router-link to="/Pagos">Registro de pagos</router-link></li>
    </ul>

    <ul class="ingreso">
      <li><router-link to="/InicioSesion">Iniciar Sesion</router-link></li>
      <li><router-link to="/Registrarse">Registrarse</router-link></li>
    </ul>

  </nav>

</template>

<style>
body {
  background-color: #f8eee7;

}

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