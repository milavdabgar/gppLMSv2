import axios from "axios";
import config from "@/config";

class ApiService {
  constructor(endpoint) {
    this.apiUrl = `${config.apiBaseUrl}/${endpoint}`;
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
  async fetchLoans(filter) {
    const loanData = await this.getAll(filter);
    return Promise.all(loanData.map(async loan => {
      const book = await bookService.getById(loan.book_id);
      loan.bookTitle = book.title;
      return loan;
    }));
  }

  async requestLoan(bookId, memberId) {
    const loan = {
      book_id: bookId,
      member_id: memberId,
      status: 'requested'
    };
    return this.create(loan);
  }

  async approveLoan(id) {
    const response = await axios.put(`${this.apiUrl}/${id}/approve`);
    return response.data;
  }

  async returnLoan(loanId) {
    const loan = await this.getById(loanId);
    if (loan.status === "approved") {
      const updatedLoanData = {
        book_id: loan.book_id,
        member_id: loan.member_id,
        status: "returned",
        returned_date: new Date().toISOString().split("T")[0],
      };
      await this.update(loanId, updatedLoanData);
    }
  }
}

class ProfileService extends ApiService {
  async getProfile(userId) {
    const response = await axios.get(`${this.apiUrl}/${userId}`);
    return response.data;
  }

  async updateProfile(userId, data) {
    const response = await axios.put(`${this.apiUrl}/${userId}`, data);
    return response.data;
  }
}

class BookService extends ApiService {
  async getByGenre(genreId) {
    const response = await axios.get(`${this.apiUrl}?filters[genre_id]=${genreId}`);
    return response.data;
  }
}



export default ApiService;

export const userService = new ApiService("api/users");
export const authorService = new ApiService("api/authors");
export const genreService = new ApiService("api/genres");
export const bookService = new BookService("api/books");
export const bookLoanService = new BookLoanService("api/bookloans");
export const profileService = new ProfileService("api/profile");