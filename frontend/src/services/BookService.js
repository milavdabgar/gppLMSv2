/**
 * Service for interacting with the books API
*/

import axios from 'axios';

const API_URL = 'http://localhost:5000/api/books';

export default {

    /**
     * Create a new book
     * @param {Object} book - Book details 
     * @returns {Promise}
    */
    async createBook(book) {
        const response = await axios.post(API_URL, book);
        return response.data;
    },

    /**
     * Get paginated books
     * @param {Object} params - Request parameters
     * @returns {Promise}
    */
    async getBooks(params = {}) {
        const response = await axios.get(API_URL, { params });
        return response.data;
    },

    /**
     * Get book details by ID
     * @param {Number} id - Book ID
     * @returns {Promise} 
    */
    async getBookById(id) {
        const response = await axios.get(`${API_URL}/${id}`);
        return response.data;
    },

    /**
     * Update book by ID
     * @param {Number} id - Book ID
     * @param {Object} book - Updated book data
     * @returns {Promise}
    */
    async updateBook(id, book) {
        const response = await axios.put(`${API_URL}/${id}`, book);
        return response.data;
    },

    /**
     * Delete book by ID
     * @param {Number} id - Book ID
     * @returns {Promise}
    */
    async deleteBook(id) {
        const response = await axios.delete(`${API_URL}/${id}`);
        return response.data;
    }
}