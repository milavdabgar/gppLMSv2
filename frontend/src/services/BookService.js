import axios from "axios";

const API_URL = "http://localhost:5000/api/books";

export default {
  async createBook(book) {
    const response = await axios.post(API_URL, book);
    return response.data;
  },

  async getBooks(params = {}) {
    const response = await axios.get(API_URL, { params });
    return response.data;
  },

  async getBookById(id) {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  },

  async updateBook(id, book) {
    const response = await axios.put(`${API_URL}/${id}`, book);
    return response.data;
  },

  async deleteBook(id) {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data;
  },
};
