<template>
    <div class="browse-genre">
      <h2>Browse Genres</h2>
      <input type="text" v-model="searchQuery" placeholder="Search genres" />
      <ul>
        <li v-for="genre in filteredGenres" :key="genre.id" @click="selectGenre(genre)">
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
        searchQuery: '',
        selectedGenre: null,
      };
    },
    computed: {
      filteredGenres() {
        return this.genres.filter(genre =>
          genre.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
      },
    },
    methods: {
      async fetchGenres() {
        this.genres = await genreService.getAll();
      },
      selectGenre(genre) {
        this.selectedGenre = genre;
        this.$emit('genre-selected', genre);
      },
    },
    created() {
      this.fetchGenres();
    },
  };
  </script>
  
  <style scoped>
  .browse-genre {
    margin-bottom: 20px;
  }
  
  .browse-genre ul {
    list-style-type: none;
    padding: 0;
  }
  
  .browse-genre li {
    cursor: pointer;
    padding: 5px;
  }
  
  .browse-genre li:hover {
    background-color: #f0f0f0;
  }
  </style>