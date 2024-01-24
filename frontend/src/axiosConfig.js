import axios from 'axios';

// Create an Axios instance
const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000/'
});

// Request Interceptor
axiosInstance.interceptors.request.use(config => {
    const token = localStorage.getItem('authToken');
    if (token) {
        config.headers['Authentication-Token'] = token;
    }
    return config;
}, error => {
    return Promise.reject(error);
});

export default axiosInstance;
