<template>
  <div class="browse-library">
    <SearchBar @search="onSearch" />
    <div class="main-content">
      <SideMenu :is-open="isSideMenuOpen" @toggle="toggleSideMenu" @filter-changed="onFilterChanged" />
      <div class="content">
        <BrowseGenre @genre-selected="onGenreSelected" />
        <BrowseBooks :search-query="searchQuery" :selected-filters="selectedFilters" @loan-created="onLoanCreated" />
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import SideMenu from '@/components/SideMenu.vue';
import BrowseGenre from '@/components/BrowseGenre.vue';
import BrowseBooks from '@/components/BrowseBooks.vue';

export default {
  components: {
    SearchBar,
    SideMenu,
    BrowseGenre,
    BrowseBooks,
  },
  data() {
    return {
      isSideMenuOpen: true,
      searchQuery: '',
      selectedFilters: {
        genres: [],
        authors: [],
        languages: [],
        ratings: [],
        types: [],
        publishers: [],
        publicationDates: [],
        freeAccessInMemberships: [],
        collections: [],
        wishlists: [],
      },
    };
  },
  methods: {
    toggleSideMenu() {
      this.isSideMenuOpen = !this.isSideMenuOpen;
    },
    onSearch(query) {
      this.searchQuery = query;
    },
    onFilterChanged(filters) {
      this.selectedFilters = { ...this.selectedFilters, ...filters };
    },
    onGenreSelected(genre) {
      this.selectedFilters.genres = [genre.id];
      this.onFilterChanged({ genres: [genre.id] });
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
}

.main-content {
  display: flex;
}

.content {
  flex: 1;
  padding: 20px;
}
</style>