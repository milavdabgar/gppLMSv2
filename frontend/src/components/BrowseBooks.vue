<template>
  <div>
    <h1>Books</h1>
    <ul>
      <li v-for="book in books" :key="book.id">
        {{ book.title }}
        <button @click="requestLoan(book.id)">Request</button>
      </li>
    </ul>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';

export default {
  data() {
    return {
      books: [],
    };
  },
  
  async created() {
    try {
      this.books = await bookService.getAll();
    } catch (error) {
      console.error(error);
    }
  },
  
  methods: {
    async requestLoan(bookId) {
      try {
        await bookLoanService.requestLoan(bookId, this.$store.state.user.id);
        this.$emit('loanCreated');
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>