import { createRouter, createWebHistory } from "vue-router";
import { CalendarioRoutes } from "./CalendarioRoutes";
import { HabitacionesRoutes } from "./HabitacionesRoutes";
import { HabitacionHuespedRoutes } from "./HabitacionHuespedRoutes";
import { HabitacionRoutes } from "./HabitacionRoutes";
import { InicioSesionRoutes } from "./InicioSesionRoutes";
import { PagosRoutes } from "./PagosRoutes";
import { RegistrarseRoutes } from "./RegistrarseRoutes";
import { ReservaHuespedRoutes } from "./ReservaHuespedRoutes";
import { ReservaRoutes } from "./ReservaRoutes";
import { BienvenidaRoutes } from "./BienvenidaRoutes";
import { ReservasRoutes } from "./ReservasRoutes";


const routes = [

    ...CalendarioRoutes,
    ...HabitacionesRoutes,
    ...HabitacionHuespedRoutes,
    ...HabitacionRoutes,
    ...InicioSesionRoutes,
    ...PagosRoutes,
    ...RegistrarseRoutes,
    ...ReservaHuespedRoutes,
    ...ReservaRoutes,
    ...BienvenidaRoutes,
    ...ReservasRoutes,


    {
        path: "/",
        redirect: "/Bienvenida",
    },

    {
        path: "/:pathMatch(.*)*",
        name: "NotFound",
        component: () => import("../views/PaginaNoEncontrada.vue"),
    },
];

const router = createRouter({
    history: createWebHistory('/'),

    routes,
});

export default router;

