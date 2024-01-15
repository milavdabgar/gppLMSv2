from flask import Blueprint
from flask import render_template, redirect, url_for
from flask_security import current_user
from .forms import UserForm, BookForm
from .models import db, user_datastore, User
from .services import create_book, get_all_books, get_book, update_book

librarian_bp = Blueprint("librarian_bp", __name__)


@librarian_bp.route("/")
def index():
    # if not current_user.is_authenticated:
    #     return url_for("security.login")
    return render_template("index.html")

@librarian_bp.route('/home')
def home():
    if current_user.roles in ['admin', 'librarian']:
        return render_template('member/home.html')
    return render_template('librarian/home.html')


@librarian_bp.route("/user/display")
def display_users():
    users = User.query.all()
    return render_template("librarian/user_list.html", users=users)


@librarian_bp.route("/user/show/<int:user_id>")
def show_user(user_id):
    user = user_datastore.find_user(id=user_id)
    if user:
        return render_template("librarian/user_view.html", user=user)
    return {"message": "User not found"}, 404


@librarian_bp.route("/user/add", methods=["GET", "POST"])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "submit"}
        user = user_datastore.create_user(**data)
        db.session.commit()
        return redirect(url_for("librarian_bp.display_users", user_id=user.id))
    return render_template("librarian/user_add.html", form=form)


@librarian_bp.route("/user/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("librarian_bp.display_users", user_id=user.id))
    return render_template("librarian/user_edit.html", form=form, user=user)


@librarian_bp.route("/user/delete/<int:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("librarian_bp.display_users", user_id=user.id))
    return render_template("librarian/user_delete.html", user=user)


# @librarian_bp.route("/books", methods=["GET", "POST"])
# def book_list():
#     form = BookForm()
#     if form.validate_on_submit():
#         data = {k: v for k, v in form.data.items() if k != "submit"}
#         create_book(data)
#         # new_book = Book(**data)
#         # db.session.add(new_book)
#         # db.session.commit()
#         return redirect(url_for("librarian_bp.book_list"))
#     books = get_all_books()
#     return render_template("book_list.html", form=form, books=books)


# @librarian_bp.route("/books/<int:book_id>", methods=["GET", "POST"])
# def edit_book(book_id):
#     book = get_book(book_id)
#     form = BookForm(obj=book)
#     if form.validate_on_submit():
#         # form.populate_obj(book)
#         # db.session.commit()
#         update_book(book_id, form.data)
#         return redirect(url_for("librarian_bp.book_list"))
#     return render_template("edit_book.html", form=form, book=book)