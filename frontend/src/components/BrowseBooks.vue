<template>
  <div class="browse-books">
    <h2>Browse Books</h2>
    <div class="controls">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Search books..."
        class="search-input"
      />
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
    <div v-if="showFilters" class="filters">
      <div v-for="(options, filterType) in filters" :key="filterType" class="filter">
        <h3>{{ filterType }}</h3>
        <div v-for="option in options" :key="option.id" class="filter-option">
          <input
            type="checkbox"
            :id="option.id"
            :value="option.id"
            v-model="selectedFilters[filterType]"
          />
          <label :for="option.id">{{ option.name || option }}</label>
        </div>
      </div>
    </div>
    <div class="book-list">
      <div v-for="book in filteredBooks" :key="book.id" class="book-item">
        <img :src="book.coverImage" alt="Book Cover" class="book-cover" />
        <div class="book-details">
          <h3>{{ book.title }}</h3>
          <p>{{ book.authors.map(author => author.name).join(', ') }}</p>
          <p>Rating: {{ book.rating }}</p>
          <button @click="requestLoan(book.id)">Request</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';

export default {
  data() {
    return {
      books: [],
      searchQuery: '',
      sortOption: '',
      showFilters: false,
      filters: {
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
    this.populateFilters();
  },
  computed: {
    filteredBooks() {
      let filtered = this.books.filter(book => {
        const matchesQuery = !this.searchQuery || book.title.toLowerCase().includes(this.searchQuery.toLowerCase());
        const matchesFilters = Object.keys(this.selectedFilters).every(filterType => {
          const filterOptions = this.selectedFilters[filterType];
          if (filterOptions.length === 0) return true;
          if (filterType === 'genres') {
            return book.genres.some(genre => filterOptions.includes(genre.id));
          } else if (filterType === 'authors') {
            return book.authors.some(author => filterOptions.includes(author.id));
          } else if (filterType === 'freeAccessInMemberships') {
            return book.free_access_in_memberships.some(membership => filterOptions.includes(membership.id));
          } else if (filterType === 'collections') {
            return book.collections.some(collection => filterOptions.includes(collection.id));
          } else if (filterType === 'wishlists') {
            return book.wishlists.some(wishlist => filterOptions.includes(wishlist.id));
          } else {
            return filterOptions.includes(book[filterType]);
          }
        });
        return matchesQuery && matchesFilters;
      });

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
    populateFilters() {
      this.filters.genres = [...new Set(this.books.flatMap(book => book.genres))].map(genre => ({ id: genre.id, name: genre.name }));
      this.filters.authors = [...new Set(this.books.flatMap(book => book.authors))].map(author => ({ id: author.id, name: author.name }));
      this.filters.languages = [...new Set(this.books.map(book => book.language))];
      this.filters.ratings = [...new Set(this.books.map(book => book.rating))];
      this.filters.types = [...new Set(this.books.map(book => book.type))];
      this.filters.publishers = [...new Set(this.books.map(book => book.publisher))];
      this.filters.publicationDates = [...new Set(this.books.map(book => book.publication_date))];
      this.filters.freeAccessInMemberships = [...new Set(this.books.flatMap(book => book.free_access_in_memberships))].map(membership => ({ id: membership.id, name: membership.name }));
      this.filters.collections = [...new Set(this.books.flatMap(book => book.collections))].map(collection => ({ id: collection.id, name: collection.name }));
      this.filters.wishlists = [...new Set(this.books.flatMap(book => book.wishlists))].map(wishlist => ({ id: wishlist.id, name: wishlist.name }));
    },
  },
};
</script>

<style scoped>
.browse-books {
  flex: 1;
  padding: 10px;
}

.controls {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.search-input {
  flex: 1;
  padding: 5px;
  margin-right: 10px;
}

.sort-select {
  margin-right: 10px;
}

.filters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 20px;
}

.filter {
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.filter-option {
  display: flex;
  align-items: center;
  margin-bottom: 5px;
}

.filter-option input {
  margin-right: 5px;
}

.book-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.book-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.book-cover {
  width: 150px;
  height: 200px;
  object-fit: cover;
  margin-bottom: 10px;
}

.book-details {
  flex: 1;
}
</style>