import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
Vue.use(Vuex);

export default new Vuex.Store({
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
        async login({ commit }, credentials) {
            try {
                const response = await axios.post('http://localhost:5000/login', credentials, {
                    params: {
                        include_auth_token: true
                    }
                });
                localStorage.setItem('authToken', response.data.response.user.authentication_token);
                // axios.defaults.headers.common['Authentication-Token'] = localStorage.authToken
                commit('SET_USER', response.data.response.user);
            } catch (error) {
                console.error('Login failed:', error);
            }
        },
        async logout({ commit }) {
            try {
                // Replace with your actual logout API request
                await axios.post('http://localhost:5000/logout');
                localStorage.removeItem('authToken');
                commit('CLEAR_USER');
            } catch (error) {
                // Handle logout error
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
