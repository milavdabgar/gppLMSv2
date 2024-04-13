<!-- src/components/BookBrowsing/BrowseGenre.vue -->
<template>
    <div class="browse-genre">
      <h2>Browse Genres</h2>
      <div class="controls">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search genres..."
          class="search-input"
        />
        <select v-model="sortOption" class="sort-select">
          <option value="">Sort by...</option>
          <option value="name-asc">Name (A-Z)</option>
          <option value="name-desc">Name (Z-A)</option>
        </select>
      </div>
      <div class="genre-list">
        <CardComponent
          v-for="genre in filteredGenres"
          :key="genre.id"
          :title="genre.name"
          @click="selectGenre(genre)"
          :class="{ selected: selectedGenre && selectedGenre.id === genre.id }"
        />
      </div>
    </div>
  </template>
  
  <script>
  import { genreService } from '@/services/ApiService';
  import CardComponent from './CardComponent';
  
  export default {
    components: {
      CardComponent,
    },
    data() {
      return {
        genres: [],
        searchQuery: '',
        sortOption: '',
        selectedGenre: null,
      };
    },
    computed: {
      filteredGenres() {
        let filtered = this.genres.filter((genre) =>
          genre.name.toLowerCase().includes(this.searchQuery.toLowerCase())
        );
  
        if (this.sortOption) {
          const [sortBy, sortOrder] = this.sortOption.split('-');
          filtered.sort((a, b) => {
            let comparison = 0;
            if (sortBy === 'name') {
              comparison = a.name.localeCompare(b.name);
            }
            return sortOrder === 'asc' ? comparison : -comparison;
          });
        }
  
        return filtered;
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
  
  .controls {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .search-input {
    flex: 1;
    padding: 5px;
    margin-right: 10px;
  }
  
  .sort-select {
    margin-right: 10px;
  }
  
  .genre-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
  }
  
  .genre-list .card {
    cursor: pointer;
  }
  
  .genre-list .card.selected {
    background-color: #f0f0f0;
  }
  </style>./CardComponent.vue