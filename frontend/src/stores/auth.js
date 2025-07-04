import { defineStore } from 'pinia'
import router from '../router'
import { login } from '../api/auth'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        access: localStorage.getItem('access_token') || null,
        refresh: localStorage.getItem('refresh_token') || null,
        user: null,
    }),
    actions: {
        async login(username, password) {
            try {
                const data = await login(username, password)
                this.access = data.access
                this.refresh = data.refresh
                localStorage.setItem('access_token', this.access)
                localStorage.setItem('refresh_token', this.refresh)
                router.push('/dashboard')
            } catch (error) {
                throw new Error('Credenciales inválidas')
            }
        },
        logout() {
            this.access = null
            this.refresh = null
            localStorage.removeItem('access_token')
            localStorage.removeItem('refresh_token')
            router.push('/')
        },
        setAccessToken(newAccess) {
            this.access = newAccess
            localStorage.setItem('access_token', newAccess)
        }
    }
})