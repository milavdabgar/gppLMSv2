<template>
  <div>
    <!-- Display user's loans -->
    <book-loans-list-component />
  </div>
</template>
  
<script>
import BookLoansListComponent from '@/components/BookLoansListComponent';

export default {
  components: {
    BookLoansListComponent
  }
};
</script>