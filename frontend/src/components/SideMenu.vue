<template>
    <div class="side-menu">
      <FilterSection title="Genres" :options="genres" @filter-changed="onFilterChanged('genres', $event)" />
      <FilterSection title="Authors" :options="authors" @filter-changed="onFilterChanged('authors', $event)" />
      <FilterSection title="Languages" :options="languages" @filter-changed="onFilterChanged('languages', $event)" />
      <FilterSection title="Ratings" :options="ratings" @filter-changed="onFilterChanged('ratings', $event)" />
    </div>
  </template>
  
  <script>
  import FilterSection from '@/components/FilterSection.vue';
  import { genreService, authorService } from '@/services/ApiService';
  
  export default {
    components: {
      FilterSection,
    },
    data() {
      return {
        genres: [],
        authors: [],
        languages: ['English', 'Spanish', 'French'],
        ratings: [5, 4, 3, 2, 1],
        selectedFilters: {
          genres: [],
          authors: [],
          languages: [],
          ratings: [],
        },
      };
    },
    async created() {
      try {
        this.genres = await genreService.getAll();
        this.authors = await authorService.getAll();
      } catch (error) {
        console.error(error);
      }
    },
    methods: {
      onFilterChanged(filterType, selectedOptions) {
        this.selectedFilters[filterType] = selectedOptions;
        this.$emit('filter-changed', this.selectedFilters);
      },
    },
  };
  </script>
  
  <style scoped>
  .side-menu {
    width: 200px;
    padding: 10px;
  }
  </style>