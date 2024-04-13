<!-- src/components/BookBrowsing/BrowseBooks.vue -->
<template>
  <div class="browse-books">
  <div class="controls">
    <input v-model="searchQuery" type="text" placeholder="Search books..." class="search-input" />
    <select v-model="sortOption" class="sort-select">
      <option value="">Sort by...</option>
      <option value="title-asc">Title (A-Z)</option>
      <option value="title-desc">Title (Z-A)</option>
      <option value="rating-asc">Rating (Low to High)</option>
      <option value="rating-desc">Rating (High to Low)</option>
    </select>
    <button @click="showFilters = !showFilters" class="filter-toggle">
      {{ showFilters ? 'Hide Filters' : 'Show Filters' }}
    </button>
  </div>

  <div class="filters-and-books">
    <div class="side-pane">
      <SideMenu v-if="showFilters" :is-open="showFilters" @toggle="showFilters = !showFilters"
        @filter-changed="onFilterChanged" />
    </div>
    <div class="book-list">
      <CardComponent v-for="book in filteredBooks" :key="book.id" :title="book.title"
        :subtitle="book.authors.map(author => author.name).join(', ')" :description="`Rating: ${book.rating}`"
        :image="book.coverImage">
        <button @click="requestLoan(book.id)">Request</button>
      </CardComponent>
    </div>
  </div>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';
import SideMenu from './SideMenu.vue';
import CardComponent from './CardComponent.vue';
import filterBooks from '@/utils/filterBooks';

export default {
  components: {
    SideMenu,
    CardComponent,
  },
  data() {
    return {
      books: [],
      searchQuery: '',
      sortOption: '',
      showFilters: false,
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
  async created() {
    this.books = await bookService.getAll();
  },
  computed: {
    filteredBooks() {
      let filtered = filterBooks(this.books, this.searchQuery, this.selectedFilters);

      if (this.sortOption) {
        const [sortBy, sortOrder] = this.sortOption.split('-');
        filtered.sort((a, b) => {
          let comparison = 0;
          if (sortBy === 'title') {
            comparison = a.title.localeCompare(b.title);
          } else if (sortBy === 'rating') {
            comparison = a.rating - b.rating;
          }
          return sortOrder === 'asc' ? comparison : -comparison;
        });
      }

      return filtered;
    },
  },
  methods: {
    async requestLoan(bookId) {
      try {
        await bookLoanService.requestLoan(bookId, this.$store.state.user.id);
        this.$emit('loan-created');
      } catch (error) {
        console.error(error);
      }
    },
    onFilterChanged(filters) {
      this.selectedFilters = { ...this.selectedFilters, ...filters };
    },
  },
};
</script>

<style scoped>

.browse-books {
  flex: 1;
  padding: 10px;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 10px;
}

.filters-and-books {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 20px;
}

.side-pane {
  border-right: 1px solid #ccc;
  overflow-y: auto;
}

.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  justify-content: start;
}

.card {
  width: 200px; 
  height: 300px; 
}

.controls {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.search-input {
  flex: 1;
  padding: 5px;
  margin-right: 10px;
}

.sort-select {
  margin-right: 10px;
}
</style>