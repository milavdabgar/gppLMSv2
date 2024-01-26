<template>
  <div>
    <h1>Welcome Librarian</h1>
    <ul>
      <li>
        <router-link to="/users">User Management</router-link>
      </li>
      <li>
        <router-link to="/books">Book Management</router-link>
      </li>
      <li>
        <router-link to="/genres">Genre Management</router-link>
      </li>
      <li>
        <router-link to="/authors">Author Management</router-link>
      </li>
    </ul>
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
  