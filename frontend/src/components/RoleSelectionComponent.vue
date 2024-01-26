<template>
    <div class="role-selection">
      <h2>Select Your Role</h2>
      <button @click="selectRole('member')">Member</button>
      <button @click="selectRole('librarian')">Librarian</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      selectRole(role) {
        // Assuming the user info is stored in Vuex and contains a property for role
        this.$store.commit('SET_USER_ROLE', role); // Update role in Vuex store if needed
  
        // Redirect based on selected role
        if (role === 'member') {
          this.$router.push('/member/home');
        } else if (role === 'librarian') {
          this.$router.push('/librarian/home');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Your CSS here */
  </style>
  