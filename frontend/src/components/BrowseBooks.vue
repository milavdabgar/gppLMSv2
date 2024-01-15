<template>
  <div>
    <h1>Browse Books</h1>
    <ul>
      <!-- List of books -->
      <li v-for="book in books" :key="book.id">
        {{ book.title }}
        <!-- Request Button -->
        <button @click="requestBook(book.id)">Request</button>
        <!-- Return Button -->
        <button @click="returnBook(book.id)">Return</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
    };
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    fetchBooks() {
      axios.get('http://localhost:5000/api/books')
        .then(response => {
          this.books = response.data;
        })
        .catch(error => {
          console.error('Error fetching books:', error);
        });
    },
    requestBook(bookId) {
      axios.post(`http://localhost:5000/api/books/${bookId}/request`)
        .then(() => {
          alert('Book request successful!');
          // Handle successful request (e.g., update book status, UI feedback)
        })
        .catch(error => {
          console.error('Error requesting book:', error);
          alert('Error requesting book.');
        });
    },
    returnBook(bookId) {
      axios.post(`http://localhost:5000/api/books/${bookId}/return`)
        .then(() => {
          alert('Book return successful!');
          // Handle successful return (e.g., update book status, UI feedback)
        })
        .catch(error => {
          console.error('Error returning book:', error);
          alert('Error returning book.');
        });
    },
  },
};
</script>
