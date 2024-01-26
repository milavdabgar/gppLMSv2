<template>
    <div>
      <h2>Change Password</h2>
      <form @submit.prevent="changePassword">
        <input 
          type="password" 
          v-model="password" 
          placeholder="Current Password" 
          required
        />
        <input 
          type="password" 
          v-model="newPassword" 
          placeholder="New Password" 
          required
        />
        <input 
          type="password" 
          v-model="newPasswordConfirm" 
          placeholder="Confirm New Password" 
          required
        />
        <button type="submit">Change Password</button>
      </form>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      password: '',
      newPassword: '',
      newPasswordConfirm: ''
    };
  },
  methods: {
    async changePassword() {
      try {
        const authToken = localStorage.getItem('authToken');
        const response = await axios.post('http://localhost:5000/change', {
          password: this.password,
          new_password: this.newPassword,
          new_password_confirm: this.newPasswordConfirm
        }, {
          headers: {
            'Authentication-Token': authToken
          }
        });
        console.log(response.data);
        // Handle success (show message, redirect, etc.)
        alert('Password Changed.');
        this.$router.push('/login');
      } catch (error) {
        console.error(error);
        // Handle error (show error message, etc.)
        alert('Password Change failed.');
      }
    }
  }
};
</script>
