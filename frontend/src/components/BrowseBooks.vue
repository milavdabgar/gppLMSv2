<template>
  <div class="browse-books">
    <h2>Books</h2>
    <div class="book-list">
      <div v-for="book in filteredBooks" :key="book.id" class="book-item">
        <img :src="book.coverImage" alt="Book Cover" class="book-cover">
        <div class="book-details">
          <h3>{{ book.title }}</h3>
          <p>by {{ book.authors.map(author => author.name).join(', ') }}</p>
          <button @click="requestLoan(book.id)">Request</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';

export default {
  props: {
    searchQuery: String,
    selectedFilters: Object,
  },
  data() {
    return {
      books: [],
    };
  },
  async created() {
    await this.fetchBooks();
  },
  computed: {
    filteredBooks() {
      let filtered = this.books;

      if (this.searchQuery) {
        filtered = filtered.filter(book =>
          book.title.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }

      if (this.selectedFilters.genres.length > 0) {
        filtered = filtered.filter(book =>
          book.genres.some(genre => this.selectedFilters.genres.includes(genre.id))
        );
      }

      if (this.selectedFilters.authors.length > 0) {
        filtered = filtered.filter(book =>
          book.authors.some(author => this.selectedFilters.authors.includes(author.id))
        );
      }

      if (this.selectedFilters.languages.length > 0) {
        filtered = filtered.filter(book =>
          this.selectedFilters.languages.includes(book.language)
        );
      }

      if (this.selectedFilters.ratings.length > 0) {
        filtered = filtered.filter(book =>
          this.selectedFilters.ratings.includes(book.rating)
        );
      }

      if (this.selectedFilters.types.length > 0) {
        filtered = filtered.filter(book =>
          this.selectedFilters.types.includes(book.type)
        );
      }

      if (this.selectedFilters.publishers.length > 0) {
        filtered = filtered.filter(book =>
          this.selectedFilters.publishers.includes(book.publisher)
        );
      }

      if (this.selectedFilters.publicationDates.length > 0) {
        filtered = filtered.filter(book =>
          this.selectedFilters.publicationDates.includes(book.publication_date)
        );
      }

      if (this.selectedFilters.freeAccessInMemberships.length > 0) {
        filtered = filtered.filter(book =>
          book.free_access_in_memberships.some(membership => this.selectedFilters.freeAccessInMemberships.includes(membership.id))
        );
      }

      if (this.selectedFilters.collections.length > 0) {
        filtered = filtered.filter(book =>
          book.collections.some(collection => this.selectedFilters.collections.includes(collection.id))
        );
      }

      if (this.selectedFilters.wishlists.length > 0) {
        filtered = filtered.filter(book =>
          book.wishlists.some(wishlist => this.selectedFilters.wishlists.includes(wishlist.id))
        );
      }

      return filtered;
    },
  },
  methods: {
    async fetchBooks() {
      try {
        this.books = await bookService.getAll();
      } catch (error) {
        console.error(error);
      }
    },
    async requestLoan(bookId) {
      try {
        await bookLoanService.requestLoan(bookId, this.$store.state.user.id);
        this.$emit('loan-created');
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.browse-books {
  flex: 1;
  padding: 10px;
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