<template>
    <div>
      <ul>
        <li v-for="loan in loans" :key="loan.id">
          {{ loan.bookTitle }} - {{ loan.status }}
          <button @click="returnLoan(loan.id)" v-if="loan.canBeReturned">Return</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import BookLoanService from '@/services/BookLoanService';
  
  export default {
    data() {
      return {
        loans: [] // This should be loaded with real data
      };
    },
    methods: {
      async returnLoan(loanId) {
        try {
          await BookLoanService.returnLoan(loanId);
          // Update UI or refetch loans
        } catch (error) {
          // Handle error
        }
      }
    },
    created() {
      // Fetch loans data here
    }
  };
  </script>
  