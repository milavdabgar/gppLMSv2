<template>
    <div>
      <h2>My Profile</h2>
      <input type="text" v-model="firstName">
      <input type="text" v-model="lastName"> 
      <button @click="saveProfile">Save Changes</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios' 
  
  export default {
    data() {
      return {
        firstName: '',
        lastName: '',
        // ... other profile data
      }
    },
    created() {
      this.fetchProfile()
    },
    methods: {
      async fetchProfile() {
        const response = await axios.get('/profile')
        // Populate this.firstName, this.lastName, etc. from response.data
      },
      async saveProfile() {
        const updatedData = { 
           firstName: this.firstName,
           lastName: this.lastName,
           // ... other changed data
        } 
        await axios.put('/profile', updatedData)
        // Display success message 
      }
    }
  }
  </script>
  