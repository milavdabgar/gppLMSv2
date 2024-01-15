<template>
  <div>
    <h1>Edit {{ type }}</h1>
    <form @submit.prevent="submitForm">
      <div v-for="(value, key) in formData" :key="key">
        <label :for="key">{{ capitalizeFirstLetter(key) }}</label>
        <input v-model="formData[key]" :id="key" type="text">
      </div>
      <button type="submit">Update</button>
    </form>
  </div>
</template>
  
<script>
import axios from 'axios';
export default {
  props: {
    type: String,
    id: [String, Number]
  },
  data() {
    return {
      formData: {}
    };
  },
  created() {
    // Fetch the data for the given id
    this.fetchData();
  },
  methods: {
    fetchData() {
      // Example: Fetch data based on type and id
      // Replace with actual API call
      axios.get(`http://localhost:5000/api/${this.type.toLowerCase()}s/${this.id}`).then(response => {
        this.formData = response.data;
      });
    },
    submitForm() {
      // Implement the API call to update the data
      axios.put(`http://localhost:5000/api/${this.type.toLowerCase()}s/${this.id}`, this.formData)
        .then(() => {
          this.$router.push(`/${this.type.toLowerCase()}s`);
        });
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }
};
</script>
  