<template>
    <div>
      <!-- Librarian dashboard content -->
      <book-loan-requests-list-component />
      <book-loans-list-component />
    </div>
  </template>
  
  <script>
  import BookLoanRequestsListComponent from '@/components/BookLoanRequestsListComponent';
  import BookLoansListComponent from '@/components/BookLoansListComponent';
  
  export default {
    components: {
      BookLoanRequestsListComponent,
      BookLoansListComponent
    }
  };
  </script>
  