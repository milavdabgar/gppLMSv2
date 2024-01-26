<template>
  <div>
    <h1>Welcome Member</h1>
    <ul>
      <li>
        <router-link to="/member/loans">MyLoansView</router-link>
      </li>
      <li>
        <router-link to="/browse-books">BrowseBooks</router-link>
      </li>
      <li>
        <router-link to="/browse-genres">BrowseGenres</router-link>
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
  