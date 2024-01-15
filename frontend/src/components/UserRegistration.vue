// src/components/Registration.vue

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
        console.log(response.data);
        // Handle post-registration logic (e.g., redirect to login page)
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>
