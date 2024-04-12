<template>
  <div class="side-menu" :class="{ 'side-menu-open': isOpen }">
    <button class="toggle-button" @click="$emit('toggle')">
      <i :class="isOpen ? 'fas fa-chevron-left' : 'fas fa-chevron-right'"></i>
    </button>
    <transition name="slide">
      <div v-if="isOpen">
        <FilterSection title="Genres" :options="genres" @filter-changed="onFilterChanged('genres', $event)" />
        <FilterSection title="Authors" :options="authors" @filter-changed="onFilterChanged('authors', $event)" />
        <FilterSection title="Languages" :options="languages" @filter-changed="onFilterChanged('languages', $event)" />
        <FilterSection title="Ratings" :options="ratings" @filter-changed="onFilterChanged('ratings', $event)" />
        <FilterSection title="Types" :options="types" @filter-changed="onFilterChanged('types', $event)" />
        <FilterSection title="Publishers" :options="publishers" @filter-changed="onFilterChanged('publishers', $event)" />
        <FilterSection title="Publication Dates" :options="publicationDates" @filter-changed="onFilterChanged('publicationDates', $event)" />
        <FilterSection title="Free Access in Memberships" :options="freeAccessInMemberships" @filter-changed="onFilterChanged('freeAccessInMemberships', $event)" />
        <FilterSection title="Collections" :options="collections" @filter-changed="onFilterChanged('collections', $event)" />
        <FilterSection title="Wishlists" :options="wishlists" @filter-changed="onFilterChanged('wishlists', $event)" />
      </div>
    </transition>
  </div>
</template>

<script>
import FilterSection from '@/components/FilterSection.vue';
import { genreService, authorService, bookService } from '@/services/ApiService';

export default {
  components: {
    FilterSection,
  },
  props: {
    isOpen: Boolean,
  },
  data() {
    return {
      genres: [],
      authors: [],
      languages: [],
      ratings: [5, 4, 3, 2, 1],
      types: [],
      publishers: [],
      publicationDates: [],
      freeAccessInMemberships: [],
      collections: [],
      wishlists: [],
      selectedFilters: {
        genres: [],
        authors: [],
        languages: [],
        ratings: [],
        types: [],
        publishers: [],
        publicationDates: [],
        freeAccessInMemberships: [],
        collections: [],
        wishlists: [],
      },
    };
  },
  async created() {
    try {
      this.genres = await genreService.getAll();
      this.authors = await authorService.getAll();
      this.languages = await this.fetchDistinctBookValues('language');
      this.types = await this.fetchDistinctBookValues('type');
      this.publishers = await this.fetchDistinctBookValues('publisher');
      this.publicationDates = await this.fetchDistinctBookValues('publication_date');
      this.freeAccessInMemberships = await this.fetchDistinctBookValues('free_access_in_memberships');
      this.collections = await this.fetchDistinctBookValues('collections');
      this.wishlists = await this.fetchDistinctBookValues('wishlists');
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    async fetchDistinctBookValues(field) {
      try {
        const books = await bookService.getAll();
        const distinctValues = [...new Set(books.map(book => book[field]))];
        return distinctValues.filter(value => value !== null);
      } catch (error) {
        console.error(error);
        return [];
      }
    },
    onFilterChanged(filterType, selectedOptions) {
      this.selectedFilters[filterType] = selectedOptions;
      this.$emit('filter-changed', this.selectedFilters);
    },
  },
};
</script>

<style scoped>
.side-menu {
  width: 200px;
  padding: 10px;
  background-color: #f0f0f0;
  transition: width 0.3s;
  overflow: hidden;
}

.side-menu-open {
  width: 300px;
}

.toggle-button {
  width: 100%;
  padding: 5px;
  background-color: #ccc;
  border: none;
  cursor: pointer;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s;
}

.slide-enter,
.slide-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}
</style>