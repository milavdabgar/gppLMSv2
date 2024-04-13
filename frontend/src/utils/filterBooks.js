// src/utils/filterBooks.js
export default function filterBooks(books, searchQuery, selectedFilters) {
    return books.filter((book) => {
      const matchesQuery = !searchQuery || book.title.toLowerCase().includes(searchQuery.toLowerCase());
      const matchesFilters = Object.keys(selectedFilters).every((filterType) => {
        const filterOptions = selectedFilters[filterType];
        if (filterOptions.length === 0) return true;
        if (filterType === 'genres') {
          return book.genres.some((genre) => filterOptions.includes(genre.id));
        } else if (filterType === 'authors') {
          return book.authors.some((author) => filterOptions.includes(author.id));
        } else if (filterType === 'freeAccessInMemberships') {
          return book.free_access_in_memberships.some((membership) => filterOptions.includes(membership.id));
        } else if (filterType === 'collections') {
          return book.collections.some((collection) => filterOptions.includes(collection.id));
        } else if (filterType === 'wishlists') {
          return book.wishlists.some((wishlist) => filterOptions.includes(wishlist.id));
        } else {
          return filterOptions.includes(book[filterType]);
        }
      });
      return matchesQuery && matchesFilters;
    });
  }