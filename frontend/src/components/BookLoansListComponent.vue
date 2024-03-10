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
            <router-link :to="{ name: 'LoanDetails', params: { id: loan.id } }">View Details</router-link>|
            <button @click="handleReturnLoan(loan.id)" :disabled="loan.status !== 'approved'">
              Return Loan
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { bookLoanService } from "@/services/ApiService";

export default {
  props: ["memberId"],

  data() {
    return {
      loans: [],
    };
  },

  async created() {
    this.loans = await bookLoanService.fetchLoans();
  },

  methods: {
    async handleReturnLoan(loanId) {
      await bookLoanService.returnLoan(loanId);
      this.loans = await bookLoanService.fetchLoans(); // Refresh the list of loans
    },
  },
};
</script>