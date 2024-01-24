import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import axios from 'axios';
// import axiosInstance from './axiosConfig';

Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [createPersistedState({
        paths: ['user'] // Specify only the state you want to persist, e.g., 'user'
    })],

    state: {
        user: null
    },
    mutations: {
        SET_USER(state, user) {
            state.user = user;
        },
        CLEAR_USER(state) {
            state.user = null;
        }
    },
    actions: {
        async register({ dispatch }, credentials) {
            try {
                const response = await axios.post('http://localhost:5000/register', credentials, {
                    params: {
                        include_auth_token: true
                    }
                });
                localStorage.setItem('authToken', response.data.response.user.authentication_token);
                axios.defaults.headers.common['Authentication-Token'] = localStorage.authToken
                await dispatch('fetchUser');
            } catch (error) {
                console.error('Login failed:', error);
            }
        },
        async login({ dispatch }, credentials) {
            try {
                const response = await axios.post('http://localhost:5000/login', credentials, {
                    params: {
                        include_auth_token: true
                    }
                });
                localStorage.setItem('authToken', response.data.response.user.authentication_token);
                axios.defaults.headers.common['Authentication-Token'] = localStorage.authToken
                await dispatch('fetchUser');
            } catch (error) {
                console.error('Login failed:', error);
            }
        },
        async fetchUser({ commit }) {
            const token = localStorage.getItem('authToken');
            if (token) {
              try {
                const userResponse = await axios.get('http://localhost:5000/api/current_user');
                commit('SET_USER', userResponse.data);
              } catch (error) {
                console.error('Error fetching user:', error);
              }
            }
          },

        async logout({ commit }) {
            try {
                await axios.post('http://localhost:5000/logout');
                localStorage.removeItem('authToken');
                axios.defaults.headers.common['Authentication-Token'] = ''; // Reset the Axios header
                commit('CLEAR_USER');
            } catch (error) {
                console.error('Logout failed:', error);
            }
        }
    },

    getters: {
        userId(state) {
            return state.user.id
        }
    }

});
