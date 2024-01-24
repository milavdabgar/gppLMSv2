from flask import Blueprint, render_template
from flask_security import auth_required
from ..models import Book
from ..routes.crud_api_calls import api_call

member_bp = Blueprint("member_bp", __name__)

@member_bp.route("/member/home")
@auth_required("token", "session")
def home():
    books = Book.query.all()
    return render_template("member/home.html", books=books)

def request_book(book_id, member_id):
    return api_call(f"books/request/{book_id}/{member_id}", method="post")


def view_loans(member_id):
    return api_call(f"loans/{member_id}", method="get")


def return_book(loan_id):
    return api_call(f"loans/return/{loan_id}", method="put")  