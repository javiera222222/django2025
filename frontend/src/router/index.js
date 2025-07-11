import { createRouter, createWebHistory } from "vue-router";
import { CalendarioRoutes } from "./CalendarioRoutes";
import { HabitacionesRoutes } from "./HabitacionesRoutes";
import { HabitacionHuespedRoutes } from "./HabitacionHuespedRoutes";
import { HabitacionRoutes } from "./HabitacionRoutes";
import { PagosRoutes } from "./PagosRoutes";
import { RegistrarseRoutes } from "./RegistrarseRoutes";
import { ReservaHuespedRoutes } from "./ReservaHuespedRoutes";
import { ReservaRoutes } from "./ReservaRoutes";
import { BienvenidaRoutes } from "./BienvenidaRoutes";
import { ReservasRoutes } from "./ReservasRoutes";
import Login from '../views/LoginView.vue'
import Dashboard from '../views/DashboardView.vue'
import { useAuthStore } from '../stores/auth'

const routes = [

    ...CalendarioRoutes,
    ...HabitacionesRoutes,
    ...HabitacionHuespedRoutes,
    ...HabitacionRoutes,
    ...PagosRoutes,
    ...RegistrarseRoutes,
    ...ReservaHuespedRoutes,
    ...ReservaRoutes,
    ...BienvenidaRoutes,
    ...ReservasRoutes,
    { path: '/', name: 'Login', component: Login },
    { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true } },



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

router.beforeEach((to, from, next) => {
    const authStore = useAuthStore()
    if (to.meta.requiresAuth && !authStore.access) {
        next('/')
    } else {
        next()
    }
})

export default router;

