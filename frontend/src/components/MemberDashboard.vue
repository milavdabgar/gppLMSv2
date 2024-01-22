<template>
    <div>
      <h1>Welcome Member</h1>
      <ul>
        <li>
            <router-link to="/browse-books">BrowseBooks</router-link>
        </li>
        <li>
        <router-link to="/browse-genres">BrowseGenres</router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MemberDashboard'
    // You can add script logic here if needed
  };
  </script>
  
  <style scoped>
  /* Add your CSS styling here */
  </style>
  