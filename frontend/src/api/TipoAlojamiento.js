import api from './index'

export const getTipoAlojamientos = async () => {
    const response = await api.get('backend/api/TipoAlojamiento/')
    return response.data
}

export const getTipoAlojamiento = async (id) => {
    const response = await api.get(`backend/api/TipoAlojamiento/${id}/`)
    return response.data
}

export const updateTipoAlojamiento = async (id, data) => {
    const response = await api.put(`backend/api/TipoAlojamiento/${id}/`, data)
    return response.data
}

export const parcialUpdateTipoAlojamiento = async (id, data) => {
    const response = await api.patch(`backend/api/TipoAlojamiento/${id}/`, data)
    return response.data
}

export const deleteTipoAlojamiento = async (id) => {
    const response = await api.delete(`backend/api/TipoAlojamiento/${id}/`)
    return response.data
}

export const createTipoAlojamiento = async (data) => {
    const response = await api.post('backend/api/TipoAlojamiento/', data)
    return response.data
}