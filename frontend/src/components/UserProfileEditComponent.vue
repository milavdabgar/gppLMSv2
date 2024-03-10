<template>
    <div class="edit-profile">
      <h2>Edit Profile</h2>
      <form @submit.prevent="updateProfile">
        <div>
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="profile.username" required>
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="profile.email" required>
        </div>
        <div>
          <label for="firstName">First Name:</label>
          <input type="text" id="firstName" v-model="profile.first_name">
        </div>
        <div>
          <label for="lastName">Last Name:</label>
          <input type="text" id="lastName" v-model="profile.last_name">
        </div>
        <button type="submit">Update Profile</button>
      </form>
    </div>
  </template>
  
  <script>
  import { profileService } from '@/services/ApiService';
  
  export default {
    data() {
      return {
        profile: {},
      };
    },
    created() {
      this.fetchProfile();
    },
    methods: {
      async fetchProfile() {
        try {
          const userId = this.$store.getters.userId;
          this.profile = await profileService.getProfile(userId);
        } catch (error) {
          console.error('Error fetching profile:', error);
        }
      },
      async updateProfile() {
        try {
          await profileService.updateProfile(this.profile.id, this.profile);
          alert('Profile updated successfully');
          this.$router.push({ name: 'Profile' });
        } catch (error) {
          console.error('Error updating profile:', error);
        }
      },
    },
  };
  </script>