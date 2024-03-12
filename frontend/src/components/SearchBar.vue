<template>
    <div class="search-bar">
      <input type="text" v-model="searchQuery" @input="onSearch" placeholder="Search books">
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',
      };
    },
    methods: {
      onSearch() {
        this.$emit('search', this.searchQuery);
      },
    },
  };
  </script>
  
  <style scoped>
  .search-bar {
    padding: 10px;
  }
  
  .search-bar input {
    width: 100%;
    padding: 5px;
    font-size: 16px;
  }
  </style>