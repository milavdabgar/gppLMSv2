<template>
  <div>
    <h1>Books</h1>
    <input type="text" v-model="searchQuery" @input="searchBooks" placeholder="Search books">
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
    selectedGenreId: {
      type: Number,
      default: null,
    },
  },
  data() {
    return {
      books: [],
      searchQuery: '',
    };
  },
  async created() {
    await this.fetchBooks();
  },
  computed: {
    filteredBooks() {
      let filtered = this.books;
      if (this.selectedGenreId) {
        filtered = filtered.filter(book =>
          book.genres.some(genre => genre.id === this.selectedGenreId)
        );
      }
      if (this.searchQuery) {
        filtered = filtered.filter(book =>
          book.title.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      }
      return filtered;
    },
  },
  methods: {
    async fetchBooks() {
      try {
        if (this.selectedGenreId) {
          this.books = await bookService.getByGenre(this.selectedGenreId);
        } else {
          this.books = await bookService.getAll();
        }
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
    async searchBooks() {
      await this.fetchBooks();
    },
  },
  watch: {
    selectedGenreId() {
      this.fetchBooks();
    },
  },
};
</script>