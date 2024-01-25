// BookLoanRequestsListComponent

<template>
  <div class="book-loan-requests">
    <h2>Loan Requests</h2>
    <table>
      <thead>
        <tr>
          <th>Loan ID</th>
          <th>Member ID</th>
          <th>Book Title</th>
          <th>Status</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="loan in loans" :key="loan.id">
          <td>{{ loan.id }}</td>
          <td> {{ loan.member_id }}</td>
          <td>{{ loan.bookTitle }}</td>
          <td>{{ loan.status }}</td>
          <td>
            <button @click="approveLoan(loan.id)">Approve</button>
            <button @click="rejectLoan(loan.id)">Reject</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script>
import BookLoanService from '@/services/BookLoanService';
import BookService from '@/services/BookService';

export default {
  data() {
    return {
      loans: []
    }
  },

  created() {
    this.fetchLoans();
  },

  methods: {
    async getBookTitle(bookId) {
      const book = await BookService.getBookById(bookId);
      return book.title;
    },

    async fetchLoans() {
      const filter = { status: 'requested' };
      const loanData = await BookLoanService.getLoans(filter);
      const loansWithTitles = await Promise.all(loanData.map(async loan => {
        const book = await BookService.getBookById(loan.book_id);
        loan.bookTitle = book.title;
        return loan;
      }));
      this.loans = loansWithTitles;
    },


    async approveLoan(id) {
      await BookLoanService.approveLoan(id);
      this.fetchLoans();
    },

    async rejectLoan(id) {
      await BookLoanService.deleteLoan(id);
      this.fetchLoans();
    }
  }
}
</script>