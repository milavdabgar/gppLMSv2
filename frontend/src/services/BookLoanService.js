import axios from "axios";

const API_URL = "http://localhost:5000/api/bookloans";

export default {
  async createLoan(loan) {
    const response = await axios.post(API_URL, loan);
    return response.data;
  },

  async getLoans(filters = {}, sort_by = {}, sort_order={}) {
    const queryParams = {
      filters: filters,
      sort_by: sort_by,
      sort_order: sort_order
    };
    const response = await axios.get(API_URL, { params: queryParams });
    return response.data;
  },
  

  async getLoanById(id) {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  },

  async updateLoan(id, loan) {
    const response = await axios.put(`${API_URL}/${id}`, loan);
    return response.data;
  },

  async deleteLoan(id) {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data;
  },

  async approveLoan(id) {
    const response = await axios.put(`${API_URL}/${id}/approve`);
    return response.data;
  },
};
