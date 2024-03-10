// config.js
const config = {
    development: {
      apiBaseUrl: "http://localhost:5000",
    },
    production: {
      apiBaseUrl: "https://api.example.com",
    },
  };
  
  export default config[process.env.NODE_ENV || "development"];