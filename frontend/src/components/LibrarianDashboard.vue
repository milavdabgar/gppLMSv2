<template>
    <div>
      <h1>Welcome Librarian</h1>
      <ul>
        <li>
          <router-link to="/users">User Management</router-link>
        </li>
        <li>
          <router-link to="/books">Book Management</router-link>
        </li>
        <li>
          <router-link to="/genres">Genre Management</router-link>
        </li>
        <li>
          <router-link to="/authors">Author Management</router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LibrarianDashboard'
    // You can add script logic here if needed
  };
  </script>
  
  <style scoped>
  /* Add your CSS styling here */
  </style>
  