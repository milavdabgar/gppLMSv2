<template>
  <div>
    <h1>Register</h1>
    <input v-model="email" type="email" placeholder="Email" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="register">Register</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://localhost:5000/register', {
          email: this.email,
          password: this.password
        });
        localStorage.setItem('authToken', response.data.response.user.authentication_token);
        axios.defaults.headers.common['Authentication-Token'] = localStorage.authToken
        alert('Registration Successful!');
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
        alert('Registration failed!');
      }
    }
  }
};
</script>
