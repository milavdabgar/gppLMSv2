<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="submitLogin">

      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="credentials.email" required>
      </div>

      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="credentials.password" required>
      </div>

      <div>
        <input type="checkbox" id="remember" v-model="credentials.remember">
        <label for="remember">Remember me</label>
      </div>

      <button type="submit">Login</button>
    </form>
    <p>
      Don't have an account? <router-link to="/register">Register</router-link>
    </p>
    <p>
      Forgot password? <router-link to="/reset">Reset</router-link>
    </p>
    <p>
      Change password: <router-link to="/change">Change</router-link>
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      credentials: { email: '', password: '', remember: false }
    };
  },
  methods: {
    async submitLogin() {
      try {
        await this.$store.dispatch('login', this.credentials);
        this.$router.push('/select_role');
      } catch (error) {
        console.log(error);
      }
    }
  }
};
</script>


