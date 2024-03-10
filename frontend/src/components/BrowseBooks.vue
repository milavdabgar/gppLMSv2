<template>
  <div>
    <h2>Books</h2>
    <input type="text" v-model="searchQuery" placeholder="Search books..." />
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
    genre: {
      type: Object,
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
      return this.books.filter(book =>
        book.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },

  methods: {
    async fetchBooks() {
      try {
        if (this.genre) {
          this.books = await bookService.getByGenre(this.genre.id);
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
  },

  watch: {
    async genre() {
      await this.fetchBooks();
    },
  },
};
</script>