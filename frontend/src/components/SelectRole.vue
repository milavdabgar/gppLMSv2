<template>
    <div>
      <h2>Select Your Role</h2>
      <form @submit.prevent="submitRole">
        <select v-model="selectedRole">
          <option disabled value="">Please select one</option>
          <option value="Librarian">Librarian</option>
          <option value="Member">Member</option>
        </select>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  // import axiosInstance from '@/axiosConfig';
  
  export default {
    data() {
      return {
        selectedRole: ''
      };
    },
    methods: {
      async submitRole() {
        try {
          const response = await axios.post('http://localhost:5000/api/select_role', {
            role: this.selectedRole
          });
          if (response.data.redirect_url) {
            window.location.href = response.data.redirect_url;
          }
        } catch (error) {
          console.error(error);
          // Handle error (show error message, etc.)
        }
      }
    }
  };
  </script>
  