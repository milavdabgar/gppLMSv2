<template>
    <div class="user-profile">
      <h2>User Profile</h2>
      <div>
        <label>Username:</label>
        <span>{{ profile.username }}</span>
      </div>
      <div>
        <label>Email:</label>
        <span>{{ profile.email }}</span>
      </div>
      <div>
        <label>First Name:</label>
        <span>{{ profile.first_name }}</span>
      </div>
      <div>
        <label>Last Name:</label>
        <span>{{ profile.last_name }}</span>
      </div>
      <button @click="editProfile">Edit Profile</button>
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
      editProfile() {
        this.$router.push({ name: 'EditProfile' });
      },
    },
  };
  </script>