<!-- src/views/BrowseLibraryView.vue -->
<template>
  <div class="browse-library">
    <BrowseGenre @genre-selected="onGenreSelected" />
    <div class="books-container">
      <BrowseBooks @loan-created="onLoanCreated" ref="browseBooks" />
    </div>
  </div>
</template>

<script>
import BrowseGenre from '@/components/BookBrowsing/BrowseGenre.vue';
import BrowseBooks from '@/components/BookBrowsing/BrowseBooks.vue';

export default {
  components: {
    BrowseGenre,
    BrowseBooks,
  },
  methods: {
    onGenreSelected(genre) {
      this.$refs.browseBooks.selectedFilters.genres = [genre.id];
    },
    onLoanCreated() {
      // Handle loan creation, e.g., show a success message
    },
  },
};
</script>

<style scoped>
.browse-library {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.main-content {
  display: flex;
  flex: 1;
}
</style>