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
import BookService from '@/services/BookService';
import BookLoanService from '@/services/BookLoanService';

export default {
  data() {
    return {
      books: [],
    };
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

    async requestLoan(selectedBookId) {
      try {
        const loan = {
          book_id: selectedBookId,
          member_id: this.$store.state.user.id,
          status: 'requested'
        };
        await BookLoanService.createLoan(loan);
        this.$emit('loanCreated');
        this.selectedBookId = null;
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
