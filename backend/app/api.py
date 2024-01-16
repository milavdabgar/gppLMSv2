from flask import Blueprint, request
from flask_restful import Resource, Api
from .models import db, user_datastore, User, Role, Book, Genre, Author, Member, Librarian
from .schemas import (
    BookSchema,
    GenreSchema,
    AuthorSchema,
    UserSchema,
    MemberSchema,
    LibrarianSchema
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
        obj = self.schema.load(request.json, session=db.session)
        db.session.add(obj)
        db.session.commit()
        return self.schema.dump(obj), 201

    def put(self, id):
        obj = self.model.query.get_or_404(id)
        updated_obj = self.schema.load(request.json, instance=obj, session=db.session)
        db.session.commit()
        return self.schema.dump(updated_obj)

    def delete(self, id):
        obj = self.model.query.get_or_404(id)
        db.session.delete(obj)
        db.session.commit()
        return '', 204


class BookApi(BaseApi):
    model = Book
    schema = BookSchema()

class GenreApi(BaseApi):
    model = Genre
    schema = GenreSchema()

class AuthorApi(BaseApi):
    model = Author
    schema = AuthorSchema()

class UserApi(BaseApi):
    model = User
    schema = UserSchema()

    # def post(self):
    #     data = self.schema.load(request.json)
    #     user = user_datastore.create_user(**data)
    #     db.session.commit()
    #     return self.schema.dump(user), 201
    def post(self):
        # Load data from request
        data = self.schema.load(request.json)

        # Extract role IDs and remove 'roles' key from data dictionary
        role_ids = data.pop('roles', [])

        # Create a new user
        user = user_datastore.create_user(**data)

        # Handle role assignments if role IDs are provided
        if role_ids:
            # Fetch roles from the database based on the provided IDs
            roles = Role.query.filter(Role.id.in_(role_ids)).all()

            # Assign these roles to the user
            user.roles = roles  # Replacing the list, assuming 'roles' is a list of role objects

        # Add the new user to the session and commit the transaction
        db.session.add(user)
        db.session.commit()

        # Return the created user
        return self.schema.dump(user), 201    

class MemberApi(UserApi):
    model = Member
    schema = MemberSchema()

class LibrarianApi(UserApi):
    model = Librarian
    schema = LibrarianSchema()


def add_resource_routes(api, resource_api_class, endpoint_name, id_type='int'):
    api.add_resource(resource_api_class, f'/api/{endpoint_name}', endpoint=f'{endpoint_name}_list')
    api.add_resource(resource_api_class, f'/api/{endpoint_name}/<{id_type}:id>', endpoint=f'{endpoint_name}')
    
# Add routes for BookApi, GenreApi, AuthorApi, etc.
add_resource_routes(api, BookApi, 'books')
add_resource_routes(api, GenreApi, 'genres')
add_resource_routes(api, AuthorApi, 'authors')    
add_resource_routes(api, UserApi, 'users')
add_resource_routes(api, MemberApi, 'members')
add_resource_routes(api, LibrarianApi, 'librarians')