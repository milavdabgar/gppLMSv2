import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
import config from "@/config";

Vue.use(Vuex);

const apiBaseUrl = config.apiBaseUrl;

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths: ["user"],
    }),
  ],

  state: {
    user: null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    SET_USER_ROLE(state, role) {
      if (state.user) {
        state.user.role = role;
      }
    },
    CLEAR_USER(state) {
      state.user = null;
    },
    CLEAR_USER_ROLE(state, role) {
      if (state.user) {
        state.user.role = role;
      }
    },
  },
  actions: {
    async register({ dispatch }, credentials) {
      try {
        const response = await axios.post(
          `${apiBaseUrl}/register`,
          credentials,
          {
            params: {
              include_auth_token: true,
            },
          }
        );
        localStorage.setItem(
          "authToken",
          response.data.response.user.authentication_token
        );
        axios.defaults.headers.common["Authentication-Token"] =
          localStorage.authToken;
        await dispatch("fetchUser");
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
    async login({ dispatch }, credentials) {
      try {
        const response = await axios.post(
          `${apiBaseUrl}/login`,
          credentials,
          {
            params: {
              include_auth_token: true,
            },
          }
        );
        localStorage.setItem(
          "authToken",
          response.data.response.user.authentication_token
        );
        axios.defaults.headers.common["Authentication-Token"] =
          localStorage.authToken;
        await dispatch("fetchUser");
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
    async fetchUser({ commit }) {
      const token = localStorage.getItem("authToken");
      if (token) {
        try {
          const userResponse = await axios.get(
            `${apiBaseUrl}/api/current_user`
          );
          commit("SET_USER", userResponse.data);
        } catch (error) {
          console.error("Error fetching user:", error);
        }
      }
    },

    async logout({ commit }) {
      try {
        await axios.post(`${apiBaseUrl}/logout`);
        localStorage.removeItem("authToken");
        axios.defaults.headers.common["Authentication-Token"] = "";
        commit("CLEAR_USER");
        commit("CLEAR_USER_ROLE");
      } catch (error) {
        console.error("Logout failed:", error);
      }
    },
  },

  getters: {
    userId(state) {
      return state.user.id;
    },
  },
});