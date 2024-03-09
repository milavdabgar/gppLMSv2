<template>
  <div>
    <h1>Genres</h1>
    <ul>
      <li v-for="genre in genres" :key="genre.id">
        {{ genre.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      genres: []
    };
  },
  async created() {
    try {
      const response = await axios.get('http://localhost:5000/api/genres');
      this.genres = response.data;
    } catch (error) {
      console.error(error);
    }
  }
};
</script>