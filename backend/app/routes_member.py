from flask import Blueprint
from flask import request, jsonify
from .models import db, Book, Genre, Author
from .schemas import book_schema, genre_schema

member_bp = Blueprint('member_bp', __name__)



@member_bp.route('/books', methods=['GET'])
def browse_books():
    query = Book.query

    # Search functionality
    title = request.args.get('title')
    author_name = request.args.get('author')
    genre_name = request.args.get('genre')

    if title:
        query = query.filter(Book.title.ilike(f'%{title}%'))
    if author_name:
        query = query.join(Book.authors).filter(Author.name.ilike(f'%{author_name}%'))
    if genre_name:
        query = query.join(Book.genres).filter(Genre.name.ilike(f'%{genre_name}%'))

    # Sorting functionality
    sort_by = request.args.get('sort_by', 'title')  # Default sort by title
    order = request.args.get('order', 'asc')        # Default order ascending

    if order == 'desc':
        query = query.order_by(db.desc(getattr(Book, sort_by)))
    else:
        query = query.order_by(getattr(Book, sort_by))

    # Execute query and return results
    books = query.all()
    return book_schema.dump(books)
