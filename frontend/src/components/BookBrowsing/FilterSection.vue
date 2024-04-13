<!-- src/components/BookBrowsing/FilterSection.vue -->
<template>
    <div class="filter-section">
      <h3>{{ title }}</h3>
      <div v-for="option in options" :key="option.id || option">
        <label>
          <input
            type="checkbox"
            :value="option.id || option"
            v-model="selectedOptions"
            @change="onFilterChanged"
          />
          {{ option.name || option }}
        </label>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      options: Array,
    },
    data() {
      return {
        selectedOptions: [],
      };
    },
    methods: {
      onFilterChanged() {
        this.$emit('filter-changed', this.selectedOptions);
      },
    },
  };
  </script>
  
  <style scoped>
  .filter-section {
    margin-bottom: 10px;
  }
  </style>