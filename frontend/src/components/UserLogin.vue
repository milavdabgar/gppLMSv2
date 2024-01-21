<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">

      <div>
        <label for="username">User Name:</label>
        <input type="username" id="username" v-model="credentials.username" required>
      </div>

      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="credentials.email" required>
      </div>

      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="credentials.password" required>
      </div>

      <div>
        <input type="checkbox" id="remember" v-model="credentials.remember">
        <label for="remember">Remember me</label>
      </div>

      <button type="submit">Login</button>
    </form>
    <p>
      Don't have an account? <router-link to="/register">Register</router-link>
    </p>

    <button @click="fetchProtectedData">Fetch Protected Data</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      credentials: {
        username: '',
        email: '',
        password: '',
        remember: false
      }
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:5000/login', this.credentials, {
          params: {
            include_auth_token: true
          }
        });
        localStorage.setItem('authToken', response.data.authentication_token);
        alert('Login Successful!');
        this.$router.push('/dashboard');
      } catch (error) {
        console.error('Login error:', error);
        alert('Login failed!');
      }
    },
    async fetchProtectedData() {
      try {
        const response = await axios.get('http://localhost:5000//member/home', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('authToken')}`
          }
        });
        console.log('Protected data:', response.data);
        alert('Protected data fetched successfully!');
      } catch (error) {
        console.error('Error fetching protected data:', error);
        alert('Failed to fetch protected data!');
      }
    }
  }
};
</script>

