from .models import db, Book, Genre

def create_book(data):
    Book.create(**data)

def get_all_books():
    return Book.query.all()

def get_book(book_id):
    return Book.query.get(book_id)

def update_book(book_id, data):
    book = Book.query.get(book_id)
    if book:
        book.update(**data)

def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book.delete()