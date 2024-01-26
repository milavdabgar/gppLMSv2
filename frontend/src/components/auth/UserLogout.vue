<template>
  <div>
    <button @click="submitLogout">Logout</button>
  </div>
</template>

<script>
export default {
  methods: {
    async submitLogout() {
      try {
        await this.$store.dispatch("logout");
        this.$router.push("/login");
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
