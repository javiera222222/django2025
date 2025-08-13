import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import router from './router'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

// Crear Vuetify
const vuetify = createVuetify({
    components,
    directives,
})

// Crear y configurar la app
const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(vuetify)

// Montar la app
app.mount('#app')
