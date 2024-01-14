# app.py
from flask import Blueprint
import requests
from flask import render_template, redirect, url_for, request
from .forms import BookForm
from .schemas import book_schema
from .models import db

api_call_bp = Blueprint('api_call_bp', __name__)

API_BASE_URL = "http://localhost:5000/api"  # Adjust as needed

def create_book(data):
    book_data = book_schema.dump(data)
    response = requests.post(f"{API_BASE_URL}/books", json=book_data)
    return response.json()


def get_all_books():
    response = requests.get(f"{API_BASE_URL}/books")
    return response.json()

def get_book(book_id):
    response = requests.get(f"{API_BASE_URL}/books/{book_id}")
    book_data = response.json()
    # Ensure that the correct session is being used
    book = book_schema.load(book_data, session=db.session)
    return book


def update_book(book_id, data):
    book_data = book_schema.dump(data)
    response = requests.put(f"{API_BASE_URL}/books/{book_id}", json=book_data)
    return response.json()

@api_call_bp.route("/")
def index():
    return render_template("librarian.html")

@api_call_bp.route("/books", methods=["GET", "POST"])
def book_list():
    form = BookForm()
    if form.validate_on_submit():
        create_book(form.data)
        return redirect(url_for("api_call_bp.book_list"))
    books = get_all_books()
    return render_template("book_list.html", form=form, books=books)


@api_call_bp.route("/books/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = get_book(book_id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        update_book(book_id, form.data)
        return redirect(url_for("api_call_bp.book_list"))
    return render_template("edit_book.html", form=form, book=book)