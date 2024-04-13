<template>
  <div class="side-menu" :class="{ open: isOpen }">
    <button
      class="toggle-button"
      @click="toggleMenu"
      aria-label="Toggle menu"
      aria-expanded="isOpen"
      aria-controls="side-menu-body"
    >
      <span class="line" :class="{ open: isOpen }"></span>
      <span class="line" :class="{ open: isOpen }"></span>
      <span class="line" :class="{ open: isOpen }"></span>
    </button>

    <transition name="slide">
      <div v-if="isOpen" id="side-menu-body" class="side-menu-body">
        <FilterSection
          v-for="filterType in filterTypes"
          :key="filterType"
          :title="filterType"
          :options="filters[filterType]"
          @filter-changed="onFilterChanged(filterType, $event)"
        />
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
      filters: {},
      selectedFilters: {},
      isLoading: true,
      isError: false,
    };
  },
  async created() {
    try {
      const filters = await this.fetchFilters();
      this.filters = filters;
      this.selectedFilters = this.initializeSelectedFilters();
    } catch (error) {
      console.error(error);
      this.isError = true;
    } finally {
      this.isLoading = false;
    }
  },
  computed: {
    filterTypes() {
      return Object.keys(this.filters);
    },
  },
  methods: {
    async fetchFilters() {
      const [genres, authors, books] = await Promise.all([
        genreService.getAll(),
        authorService.getAll(),
        bookService.getAll(),
      ]);

      const distinctBookValues = new Map();
      books.forEach((book) => {
        for (const field of [
          'language',
          'type',
          'publisher',
          'publication_date',
          'free_access_in_memberships',
          'collections',
          'wishlists',
        ]) {
          const value = book[field];
          if (value !== null) {
            const set = distinctBookValues.get(field) || new Set();
            set.add(value);
            distinctBookValues.set(field, set);
          }
        }
      });

      return {
        genres,
        authors,
        languages: [...distinctBookValues.get('language')],
        ratings: [5, 4, 3, 2, 1],
        types: [...distinctBookValues.get('type')],
        publishers: [...distinctBookValues.get('publisher')],
        publicationDates: [...distinctBookValues.get('publication_date')],
        freeAccessInMemberships: [...distinctBookValues.get('free_access_in_memberships')],
        collections: [...distinctBookValues.get('collections')],
        wishlists: [...distinctBookValues.get('wishlists')],
      };
    },
    initializeSelectedFilters() {
      return Object.fromEntries(Object.keys(this.filters).map((key) => [key, []]));
    },
    onFilterChanged(filterType, selectedOptions) {
      this.selectedFilters[filterType] = selectedOptions;
      this.$emit('filter-changed', this.selectedFilters);
    },
    toggleMenu() {
      this.$emit('toggle');
    },
  },
};
</script>

<style scoped>
.side-menu {
  height: 100%;
}

.side-menu.open {
  width: 300px;
}

.toggle-button {
  position: absolute;
  top: 10px;
  left: 10px;
  width: 30px;
  height: 24px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  z-index: 1;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.line {
  width: 100%;
  height: 3px;
  background-color: #333;
  transition: transform 0.3s, width 0.3s;
}

.line.open:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}

.line.open:nth-child(2) {
  transform: scaleX(0);
}

.line.open:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

.side-menu-body {
  padding: 10px;
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