# app.py
from flask import Blueprint, render_template, redirect, url_for
from .forms import BookForm, GenreForm, AuthorForm
from .schemas import book_schema, genre_schema, author_schema
from .models import db
import requests

api_call_bp = Blueprint("api_call_bp", __name__)

API_BASE_URL = "http://localhost:5000/api"  # Adjust as needed


# Generalized API call function
def api_call(endpoint, method="get", data=None, id=None, schema=None):
    url = f"{API_BASE_URL}/{endpoint}"
    if id:
        url += f"/{id}"

    if method == "get":
        response = requests.get(url)
    elif method in ["post", "put"]:
        if schema is not None:
            serialized_data = schema.dump(data)
        else:
            serialized_data = data
        if method == "post":
            response = requests.post(url, json=serialized_data)
        elif method == "put":
            response = requests.put(url, json=serialized_data)

    return response.json()


def handle_form_submission(
    form_class,
    schema,
    endpoint,
    template,
    redirect_endpoint,
    list_title,
    edit_title,
    edit_route,
    display_fields,
    id=None,
):
    form = form_class()
    if form.validate_on_submit():
        api_call(
            endpoint,
            method="post" if not id else "put",
            data=form.data,
            id=id,
            schema=schema,
        )
        return redirect(url_for(redirect_endpoint))

    if id:
        item_data = api_call(endpoint, id=id)
        item = schema.load(item_data, session=db.session)
        form = form_class(obj=item)

    items = api_call(endpoint) if not id else None
    return render_template(
        template,
        form=form,
        items=items,
        list_title=list_title,
        edit_title=edit_title,
        edit_route=edit_route,
        display_fields=display_fields
    )


@api_call_bp.route("/")
def index():
    return render_template("librarian.html")

# Existing book_list function
@api_call_bp.route("/books", methods=["GET", "POST"])
def book_list():
    display_fields = [("title", "isbn_13")]
    return handle_form_submission(
        BookForm,
        book_schema,
        "books",
        "list.html",
        "api_call_bp.book_list",
        "Book List",
        "Edit Book",
        "api_call_bp.edit_book",
        display_fields=display_fields
    )

# Edit book function
@api_call_bp.route("/books/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    display_fields = [("title", "isbn_13")]
    return handle_form_submission(
        BookForm,
        book_schema,
        "books",
        "edit.html",
        "api_call_bp.book_list",
        None,
        "Edit Book",
        None,
        id=id,
        display_fields=display_fields
    )

# Genre list function
@api_call_bp.route("/genres", methods=["GET", "POST"])
def genre_list():
    display_fields = [("name", "description")]
    return handle_form_submission(
        GenreForm,
        genre_schema,
        "genres",
        "list.html",
        "api_call_bp.genre_list",
        "Genre List",
        "Edit Genre",
        "api_call_bp.edit_genre",
        display_fields=display_fields
    )

# Edit genre function
@api_call_bp.route("/genres/<int:id>", methods=["GET", "POST"])
def edit_genre(id):
    display_fields = [("name", "description")]
    return handle_form_submission(
        GenreForm,
        genre_schema,
        "genres",
        "edit.html",
        "api_call_bp.genre_list",
        None,
        "Edit Genre",
        None,
        id=id,
        display_fields=display_fields
    )

# Author list function
@api_call_bp.route("/authors", methods=["GET", "POST"])
def author_list():
    display_fields = [("name", "biography")]
    return handle_form_submission(
        AuthorForm,
        author_schema,
        "authors",
        "list.html",
        "api_call_bp.author_list",
        "Author List",
        "Edit Author",
        "api_call_bp.edit_author",
        display_fields=display_fields
    )

# Edit author function
@api_call_bp.route("/authors/<int:id>", methods=["GET", "POST"])
def edit_author(id):
    display_fields = [("name", "biography")]
    return handle_form_submission(
        AuthorForm,
        author_schema,
        "authors",
        "edit.html",
        "api_call_bp.author_list",
        None,
        "Edit Author",
        None,
        id=id,
        display_fields=display_fields
    )
