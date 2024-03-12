<template>
  <div class="browse-library">
    <SearchBar @search="onSearch" />
    <div class="main-content">
      <SideMenu @filter-changed="onFilterChanged" />
      <BrowseBooks :search-query="searchQuery" :selected-filters="selectedFilters" @loan-created="onLoanCreated" />
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import SideMenu from '@/components/SideMenu.vue';
import BrowseBooks from '@/components/BrowseBooks.vue';

export default {
  components: {
    SearchBar,
    SideMenu,
    BrowseBooks,
  },
  data() {
    return {
      searchQuery: '',
      selectedFilters: {
        genres: [],
        authors: [],
        languages: [],
        ratings: [],
      },
    };
  },
  methods: {
    onSearch(query) {
      this.searchQuery = query;
    },
    onFilterChanged(filters) {
      this.selectedFilters = filters;
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
</style>