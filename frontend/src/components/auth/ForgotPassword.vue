<template>
  <div>
    <h2>Forgot Password</h2>
    <form @submit.prevent="submitEmail">
      <input type="email" v-model="email" placeholder="Enter your email" required />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import config from "@/config";
const apiBaseUrl = config.apiBaseUrl;

export default {
  data() {
    return {
      email: ''
    };
  },
  methods: {
    async submitEmail() {
      try {
        const response = await axios.post(`${apiBaseUrl}/reset`, {
          email: this.email
        });
        console.log(response.data);
        // Handle success (show message, redirect, etc.)
        alert('Reset link sent to mail');
        this.$router.push('/login');
      } catch (error) {
        console.error(error);
        alert('Password Reset failed!');
      }
    }
  }
};
</script>
