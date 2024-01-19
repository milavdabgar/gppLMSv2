from flask import Blueprint, request
from flask_restful import Resource, Api
from app.models import (
    db,
    user_datastore,
    User,
    Book,
    Genre,
    Author,
    Member,
    Librarian,
)
from app.schemas import (
    BookSchema,
    GenreSchema,
    AuthorSchema,
    UserSchema,
    MemberSchema,
    LibrarianSchema,
)


api_bp = Blueprint("api_bp", __name__)
api = Api(api_bp)


# Base API class
class BaseApi(Resource):
    model = None
    schema = None

    def get(self, id=None):
        if id:
            obj = self.model.query.get_or_404(id)
            return self.schema.dump(obj)
        else:
            objs = self.model.query.all()
            return self.schema.dump(objs, many=True)

    def post(self):
        obj = self.schema.load(request.json)
        db.session.add(obj)
        db.session.commit()
        return self.schema.dump(obj), 201

    def put(self, id):
        obj = self.model.query.get_or_404(id)
        updated_obj = self.schema.load(request.json, instance=obj)
        db.session.commit()
        return self.schema.dump(updated_obj)

    def delete(self, id):
        obj = self.model.query.get_or_404(id)
        db.session.delete(obj)
        db.session.commit()
        return "", 204


class UserApi(BaseApi):
    model = User
    schema = UserSchema()

    def post(self):
        schema = UserSchema(load_instance=False)
        data = schema.load(request.json)
        user = user_datastore.create_user(**data)
        db.session.add(user)
        db.session.commit()
        return self.schema.dump(user), 201


class MemberApi(UserApi):
    model = Member
    schema = MemberSchema()


class LibrarianApi(UserApi):
    model = Librarian
    schema = LibrarianSchema()


class BookApi(BaseApi):
    model = Book
    schema = BookSchema()


class GenreApi(BaseApi):
    model = Genre
    schema = GenreSchema()


class AuthorApi(BaseApi):
    model = Author
    schema = AuthorSchema()


def add_resource_routes(api, resource_api_class, endpoint_name, id_type="int"):
    api.add_resource(
        resource_api_class, f"/api/{endpoint_name}", endpoint=f"{endpoint_name}_list"
    )
    api.add_resource(
        resource_api_class,
        f"/api/{endpoint_name}/<{id_type}:id>",
        endpoint=f"{endpoint_name}",
    )


# Add routes for BookApi, GenreApi, AuthorApi, etc.
add_resource_routes(api, BookApi, "books")
add_resource_routes(api, GenreApi, "genres")
add_resource_routes(api, AuthorApi, "authors")
add_resource_routes(api, UserApi, "users")
add_resource_routes(api, MemberApi, "members")
add_resource_routes(api, LibrarianApi, "librarians")
