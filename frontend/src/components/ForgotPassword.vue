<template>
    <div>
      <h1>Send password reset instructions</h1>
      
      <form @submit.prevent="submit">
        <div>
          <label>Email</label>
          <input v-model="email" type="email">
          <div v-if="error">{{ error }}</div>
        </div>
  
        <button>Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: '',
        error: null
      }
    },
  
    methods: {
      async submit() {
        try {
          // Call API to send reset email 
          await this.$http.post('http://localhost:5000/reset', {email: this.email})
        //   this.$router.push('/reset-email-sent')
        } catch (err) {
          this.error = err.response.data.message
        }
      }
    }
  }
  </script>