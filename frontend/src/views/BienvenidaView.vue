<template>

    <body>


        <div class="texto">
            <h1>Bienvenido<br>
                Reserva tu alojamiento <br>
                Con los mejores precios<br>
            </h1>
        </div>
    </body>
</template>
<style>
body {
    background-image: url('../../public/inicio.svg');
    background-size: cover;
    background-position: 0% 28%;
}

.texto {
    position: absolute;
    width: 500px;
    height: 410px;
    background-color: #fff;
    top: 160px;
    left: 60px;
    padding-top: 120px;
    padding-left: 50px;
    font-size: 19px;
}

h1 {
    color: #29a5d7;
}
</style>


<!--<script>
import axios from 'axios';

export default {
    data() {
        return {
            Usuario: []
        };
    },
    mounted() {
        axios.get('/api/tasks/')
            .then(response => {
                this.tasks = response.data;
            });
    }
};

</script>-->