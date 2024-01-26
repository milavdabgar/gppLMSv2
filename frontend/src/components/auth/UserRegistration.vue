<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="submitRegister">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="credentials.email" required />
      </div>

      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="credentials.password" required />
      </div>

      <button type="submit">Register</button>
    </form>

    <p>Already have an account? <router-link to="/login">Login</router-link></p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      credentials: { email: "", password: "" },
    };
  },
  methods: {
    async submitRegister() {
      try {
        await this.$store.dispatch("register", this.credentials);
        this.$router.push("/select-role");
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
