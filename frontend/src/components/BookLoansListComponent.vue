// BookLoansListComponent

<template>
  <div class="book-loan-lists">
    <h2>Book Loans</h2>
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
          <td>{{ loan.member_id }}</td>
          <td>{{ loan.bookTitle }}</td>
          <td>{{ loan.status }}</td>
          <td>
            <router-link :to="{ name: 'LoanDetails', params: { id: loan.id } }"
              >View Details</router-link
            >| 
            <button @click="returnLoan(loan)" v-if="canReturn(loan)">
              Return Loan
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import BookLoanService from "@/services/BookLoanService";
import BookService from "@/services/BookService";

export default {
  props: ["memberId"],

  data() {
    return {
      loans: [],
    };
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
      const filter = { status: "requested" };
      const loanData = await BookLoanService.getLoans(filter);
      const loansWithTitles = await Promise.all(
        loanData.map(async (loan) => {
          const book = await BookService.getBookById(loan.book_id);
          loan.bookTitle = book.title;
          return loan;
        })
      );
      this.loans = loansWithTitles;
    },

    canReturn(loan) {
      return loan.status === "approved";
    },

    async returnLoan(loan) {
      const updatedLoanData = {
        book_id: loan.book_id, // Include the original book_id
        member_id: loan.member_id, // Include the original member_id
        status: "returned",
        returned_date: new Date().toISOString().split("T")[0], // Formats current date to YYYY-MM-DD
      };
      console.log(loan.id);
      await BookLoanService.updateLoan(loan.id, updatedLoanData);
      this.fetchLoans(); // Refresh the list of loans
    },
  },
};
</script>
