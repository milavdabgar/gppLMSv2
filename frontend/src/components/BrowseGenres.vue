<template>
  <div>
    <h2>Genres</h2>
    <ul>
      <li v-for="genre in genres" :key="genre.id" @click="selectGenre(genre)">
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

  methods: {
    selectGenre(genre) {
      this.$emit('genre-selected', genre);
    },
  },
};
</script>