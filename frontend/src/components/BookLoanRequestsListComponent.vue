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
          <td>{{ loan.member_id }}</td>
          <td>{{ loan.bookTitle }}</td>
          <td>{{ loan.status }}</td>
          <td>
            <button @click="handleLoanAction(loan.id, 'approve')">Approve</button>
            <button @click="handleLoanAction(loan.id, 'reject')">Reject</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { bookLoanService } from '@/services/ApiService';

export default {
  data() {
    return {
      loans: []
    }
  },

  async created() {
    await this.fetchLoans();
  },

  methods: {
    async fetchLoans() {
      const filter = { status: 'requested' };
      this.loans = await bookLoanService.fetchLoans(filter);
    },

    async handleLoanAction(id, action) {
      if (action === 'approve') {
        await bookLoanService.approveLoan(id);
      } else if (action === 'reject') {
        await bookLoanService.delete(id);
      }
      await this.fetchLoans();
    }
  }
}
</script>