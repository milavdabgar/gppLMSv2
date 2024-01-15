<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/books">Books</router-link> |
      <router-link to="/genres">Genres</router-link> |
      <router-link to="/authors">Authors</router-link> | 
      <router-link to="/browse-books">BrowseBooks</router-link> | 
      <router-link to="/browse-genres">BrowseGenres</router-link>
    </nav>
    <nav>
      <router-link to="/register">Register</router-link> |  
      <router-link to="/login">Login</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
