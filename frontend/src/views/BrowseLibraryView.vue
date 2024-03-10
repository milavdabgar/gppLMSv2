<template>
    <div>
      <h1>Browse Library</h1>
      <BrowseGenres @genre-selected="onGenreSelected" />
      <BrowseBooks :genre="selectedGenre" @loan-created="onLoanCreated" />
    </div>
  </template>
  
  <script>
  import BrowseBooks from '@/components/BrowseBooks.vue';
  import BrowseGenres from '@/components/BrowseGenres.vue';
  
  export default {
    components: {
      BrowseBooks,
      BrowseGenres,
    },
  
    data() {
      return {
        selectedGenre: null,
      };
    },
  
    methods: {
      onGenreSelected(genre) {
        this.selectedGenre = genre;
      },
  
      onLoanCreated() {
        // Handle loan creation, e.g., show a success message
      },
    },
  };
  </script>