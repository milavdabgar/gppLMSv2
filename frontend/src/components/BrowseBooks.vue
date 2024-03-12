<template>
  <div class="browse-books">
    <h2>Books</h2>
    <ul>
      <li v-for="book in filteredBooks" :key="book.id">
        {{ book.title }}
        <button @click="requestLoan(book.id)">Request</button>
      </li>
    </ul>
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
</style>