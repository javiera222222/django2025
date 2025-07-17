import api from './index'

export const getTipoHabitacions = async () => {
    const response = await api.get('backend/api/TipoHabitacion/')
    return response.data
}

export const getTipoHabitacion = async (id) => {
    const response = await api.get(`backend/api/TipoHabitacion/${id}/`)
    return response.data
}

export const updateTipoHabitacion = async (id, data) => {
    const response = await api.put(`backend/api/TipoHabitacion/${id}/`, data)
    return response.data
}

export const parcialUpdateTipoHabitacion = async (id, data) => {
    const response = await api.patch(`backend/api/TipoHabitacion/${id}/`, data)
    return response.data
}

export const deleteTipoHabitacion = async (id) => {
    const response = await api.delete(`backend/api/TipoHabitacion/${id}/`)
    return response.data
}

export const createTipoHabitacion = async (data) => {
    const response = await api.post('backend/api/TipoHabitacion/', data)
    return response.data
}