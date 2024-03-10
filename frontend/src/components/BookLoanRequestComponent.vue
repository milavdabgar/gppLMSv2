<template>
  <div>
    <h2>Request a Book Loan</h2>
    <form @submit.prevent="requestLoan">
      <label for="book">Book:</label>
      <select v-model="selectedBookId">
        <option v-for="book in books" :key="book.id" :value="book.id">
          {{ book.title }}
        </option>
      </select>
      <button type="submit">Request Loan</button>
    </form>
  </div>
</template>

<script>
import { bookService, bookLoanService } from '@/services/ApiService';

export default {
  data() {
    return {
      books: [],
      selectedBookId: null
    }
  },

  async created() {
    try {
      this.books = await bookService.getAll();
    } catch (error) {
      console.error(error);
    }
  },

  methods: {
    async requestLoan() {
      try {
        await bookLoanService.requestLoan(this.selectedBookId, this.$store.state.user.id);
        this.selectedBookId = null;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>