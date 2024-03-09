import axios from "axios";

class ApiService {
  constructor(apiUrl) {
    this.apiUrl = apiUrl;
  }

  async create(data) {
    const response = await axios.post(this.apiUrl, data);
    return response.data;
  }

  async getAll(filters = {}, sort_by = {}, sort_order = {}) {
    const queryParams = {
      filters: filters,
      sort_by: sort_by,
      sort_order: sort_order,
    };
    const response = await axios.get(this.apiUrl, { params: queryParams });
    return response.data;
  }

  async getById(id) {
    const response = await axios.get(`${this.apiUrl}/${id}`);
    return response.data;
  }

  async update(id, data) {
    const response = await axios.put(`${this.apiUrl}/${id}`, data);
    return response.data;
  }

  async delete(id) {
    const response = await axios.delete(`${this.apiUrl}/${id}`);
    return response.data;
  }
}

class BookLoanService extends ApiService {
  async approveLoan(id) {
    const response = await axios.put(`${this.apiUrl}/${id}/approve`);
    return response.data;
  }
}


export default ApiService;

export const userService = new ApiService("http://localhost:5000/api/users");
export const authorService = new ApiService("http://localhost:5000/api/authors");
export const genreService = new ApiService("http://localhost:5000/api/genres");
export const bookService = new ApiService("http://localhost:5000/api/books");
export const bookLoanService = new BookLoanService("http://localhost:5000/api/bookloans");
