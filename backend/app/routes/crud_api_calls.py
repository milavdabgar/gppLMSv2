from flask import Blueprint, render_template, redirect, url_for
from ..forms import BookForm, GenreForm, AuthorForm, UserForm
from ..schemas import book_schema, genre_schema, author_schema, user_schema
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

    if response.status_code == 200:
        return response.json()
    else:
        return response.text


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
        item = schema.load(item_data)
        form = form_class(obj=item)

    items = api_call(endpoint) if not id else None
    return render_template(
        template,
        form=form,
        items=items,
        list_title=list_title,
        edit_title=edit_title,
        edit_route=edit_route,
        display_fields=display_fields,
    )


# Existing book_list function
@api_call_bp.route("/books", methods=["GET", "POST"])
def book_list():
    display_fields = [("title", "isbn_13")]
    return handle_form_submission(
        form_class=BookForm,
        schema=book_schema,
        endpoint="books",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.book_list",
        list_title="Book List",
        edit_title="Edit Book",
        edit_route="api_call_bp.edit_book",
        display_fields=display_fields,
    )


# Edit book function
@api_call_bp.route("/books/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    display_fields = [("title", "isbn_13")]
    return handle_form_submission(
        form_class=BookForm,
        schema=book_schema,
        endpoint="books",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.book_list",
        list_title=None,
        edit_title="Edit Book",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


# Genre list function
@api_call_bp.route("/genres", methods=["GET", "POST"])
def genre_list():
    display_fields = [("name", "description")]
    return handle_form_submission(
        form_class=GenreForm,
        schema=genre_schema,
        endpoint="genres",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.genre_list",
        list_title="Genre List",
        edit_title="Edit Genre",
        edit_route="api_call_bp.edit_genre",
        display_fields=display_fields,
    )


# Edit genre function
@api_call_bp.route("/genres/<int:id>", methods=["GET", "POST"])
def edit_genre(id):
    display_fields = [("name", "description")]
    return handle_form_submission(
        form_class=GenreForm,
        schema=genre_schema,
        endpoint="genres",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.genre_list",
        list_title=None,
        edit_title="Edit Genre",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


# Author list function
@api_call_bp.route("/authors", methods=["GET", "POST"])
def author_list():
    display_fields = [("name", "biography")]
    return handle_form_submission(
        form_class=AuthorForm,
        schema=author_schema,
        endpoint="authors",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.author_list",
        list_title="Author List",
        edit_title="Edit Author",
        edit_route="api_call_bp.edit_author",
        display_fields=display_fields,
    )


# Edit author function
@api_call_bp.route("/authors/<int:id>", methods=["GET", "POST"])
def edit_author(id):
    display_fields = [("name", "biography")]
    return handle_form_submission(
        form_class=AuthorForm,
        schema=author_schema,
        endpoint="authors",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.author_list",
        list_title=None,
        edit_title="Edit Author",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


@api_call_bp.route("/users", methods=["GET", "POST"])
def user_list():
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=UserForm,
        schema=user_schema,
        endpoint="users",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.user_list",
        list_title="User List",
        edit_title="Edit User",
        edit_route="api_call_bp.edit_user",
        display_fields=display_fields,
    )


# Edit user function
@api_call_bp.route("/users/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=UserForm,
        schema=user_schema,
        endpoint="users",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.user_list",
        list_title=None,
        edit_title="Edit User",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )
