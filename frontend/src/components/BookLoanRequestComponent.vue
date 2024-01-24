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
import BookLoanService from '@/services/BookLoanService';
import BookService from '@/services/BookService';

export default {
  data() {
    return {
      books: [],
      selectedBookId: null
    }
  },

  created() {
    this.loadBooks();
  },

  methods: {
    async loadBooks() {
      try {
        this.books = await BookService.getBooks();
      } catch (error) {
        console.error(error);
      }
    },

    async requestLoan() {
      try {
        const loan = {
          book_id: this.selectedBookId,
          member_id: this.$store.state.user.id,
          status: 'requested'
        };
        console.log(loan)
        await BookLoanService.createLoan(loan);
        this.$emit('loanCreated');
        this.selectedBookId = null;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>