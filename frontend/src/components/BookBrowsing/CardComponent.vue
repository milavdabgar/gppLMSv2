<!-- src/components/BookBrowsing/CardComponent -->
<template>
    <div class="card">
      <img :src="image" alt="Card Image" class="card-image" />
      <div class="card-content">
        <h3 class="card-title">{{ title }}</h3>
        <p class="card-subtitle">{{ subtitle }}</p>
        <p class="card-description">{{ description }}</p>
        <div class="card-actions">
          <slot></slot>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      subtitle: String,
      description: String,
      image: String,
    },
  };
  </script>
  
  <style scoped>
  .card {
    display: flex;
    flex-direction: column;
    background-color: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    overflow: hidden;
  }
  
  .card-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }
  
  .card-content {
    padding: 16px;
  }
  
  .card-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 8px;
  }
  
  .card-subtitle {
    font-size: 14px;
    color: #666;
    margin-bottom: 8px;
  }
  
  .card-description {
    font-size: 14px;
    margin-bottom: 16px;
  }
  
  .card-actions {
    display: flex;
    justify-content: flex-end;
  }
  </style>