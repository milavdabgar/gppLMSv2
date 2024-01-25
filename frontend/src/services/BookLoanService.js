/**
 * Service for interacting with the book loans API
*/

import axios from 'axios';

const API_URL = 'http://localhost:5000/api/bookloans';

export default {

  /**
   * Create a new loan
   * @param {Object} loan - Loan details 
   * @returns {Promise}
  */
  async createLoan(loan) {
    const response = await axios.post(API_URL, loan);
    return response.data;
  },

  /**
   * Get paginated loans
   * @param {Object} params - Request parameters
   * @returns {Promise}
  */
  async getLoans(params = {}) {
    const response = await axios.get(API_URL, { params });
    console.log(response);
    return response.data;
  },

  /**
   * Get loan details by ID
   * @param {Number} id - Loan ID
   * @returns {Promise} 
  */
  async getLoanById(id) {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  },

  /**
   * Update loan by ID
   * @param {Number} id - Loan ID
   * @param {Object} loan - Updated loan data
   * @returns {Promise}
  */
  async updateLoan(id, loan) {
    const response = await axios.put(`${API_URL}/${id}`, loan);
    return response.data;
  },

  /**
   * Delete loan by ID
   * @param {Number} id - Loan ID
   * @returns {Promise}
  */
  async deleteLoan(id) {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data;
  },

  /**
   * Approve loan by ID
   * @param {Number} id - Loan ID
   * @returns {Promise}
  */
  async approveLoan(id) {
    const response = await axios.put(`${API_URL}/${id}/approve`);
    return response.data;
  }

}