<template>
  <div class="book-loan-details">
    <h2>Loan Details</h2>
    <div>
      <h3>ID: {{ loanDetails.id }}</h3>
      <p>Book ID : {{ loanDetails.book_id }}</p>
      <p>Member ID: {{ loanDetails.member_id }}</p>
      <p>Loan Date: {{ loanDetails.loan_date }}</p>
      <p>Due Date: {{ loanDetails.due_date }}</p>
      <p>Status: {{ loanDetails.status }}</p>
    </div>

    <form @submit.prevent="updateLoanDetails">
      <select v-model="loanDetails.status">
        <option>requested</option>
        <option>approved</option>
      </select>
      <button type="submit">Update Loan</button>
    </form>
  </div>
</template>

<script>
import BookLoanService from "@/services/BookLoanService";

export default {
  computed: {
    loanId() {
      return this.$route.params.id
    }
  },
  data() {
    return {
      loanDetails: {},
    };
  },
  created() {
    this.fetchLoanDetails();
  },
  methods: {
    async fetchLoanDetails() {
      this.loanDetails = await BookLoanService.getLoanById(this.loanId);
    },
    async updateLoanDetails() {
      await BookLoanService.updateLoan(this.loanId, this.loanDetails);
    },
  },
};
</script>

<style scoped>
/* Your CSS here */
</style>
