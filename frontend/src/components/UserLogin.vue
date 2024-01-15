<template>
  <div>
    <h1>Login</h1>
    <input v-model="email" type="email" placeholder="Email" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">Login</button>
    <p v-if="errorMessage">{{ errorMessage }}</p>
    <p>
      Don't have an account? <router-link to="/register">Register</router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: null
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
        });
        console.log(response.data);
        // Store the token
        localStorage.setItem('authToken', response.data.auth_token);
        // Redirect to a new route, e.g., dashboard
        this.$router.push('/dashboard');
      } catch (error) {
        this.errorMessage = 'Login failed. Please check your credentials.';
        console.error(error);
      }
    }
  }
};
</script>
