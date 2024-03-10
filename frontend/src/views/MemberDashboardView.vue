<template>
  <div>
    <h1>Welcome Member</h1>
    <ul>
      <li>
        <router-link to="/member/loans">Member Loans</router-link>
      </li>
      <li>
        <router-link to="/member/profile">Member Profile</router-link>
      </li>
      <li>
        <router-link to="/browse-books">Browse Books</router-link>
      </li>
      <li>
        <router-link to="/browse-genres">Browse Genres</router-link>
      </li>
      <li>
        <router-link to="/member/library">Browse Library</router-link>
      </li>
    </ul>
    <book-loan-request-component />
    <book-loans-list-component />
  </div>
</template>

<script>
import BookLoanRequestComponent from '@/components/BookLoanRequestComponent';
import BookLoansListComponent from '@/components/BookLoansListComponent';

export default {
  components: {
    BookLoanRequestComponent,
    BookLoansListComponent
  }
};
</script>