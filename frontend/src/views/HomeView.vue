<template>
  <div>
    <browse-books> </browse-books>
    <browse-genres> </browse-genres>
  </div>
</template>

<script>
import BrowseBooks from "@/components/BrowseBooks.vue";
import BrowseGenres from "@/components/BrowseGenres.vue";

export default {
  components: {
    BrowseBooks,
    BrowseGenres,
  },
};
</script>
