<template>
    <div>
      <button @click="logout">Logout</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        // Remove the token from local storage
        localStorage.removeItem('authToken');
  
        // Redirect the user to the login page or home page
        this.$router.push('/login');
      }
    },
    mounted() {
      // Automatically call logout when the component is mounted
      this.logout();
    }
  };
  </script>
  