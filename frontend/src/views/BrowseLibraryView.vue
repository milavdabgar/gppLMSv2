<template>
  <div>
    <h1>Browse Library</h1>
    <BrowseGenres @genre-selected="onGenreSelected" />
    <BrowseBooks :key="selectedGenreId" @loan-created="onLoanCreated" />
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
      selectedGenreId: null,
    };
  },

  methods: {
    onGenreSelected(genre) {
      this.selectedGenreId = genre.id;
    },

    onLoanCreated() {
      // Handle loan creation, e.g., show a success message
    },
  },
};
</script>