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
import { genreService } from '@/services/ApiService';

export default {
  data() {
    return {
      genres: [],
    };
  },
  async created() {
    try {
      this.genres = await genreService.getAll();
    } catch (error) {
      console.error(error);
    }
  },
};
</script>