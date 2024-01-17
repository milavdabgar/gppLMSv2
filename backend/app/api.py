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

def create_user_with_roles(data):
    print("Received data:", data)

    role_ids = data.pop('roles', [])
    print("Extracted role IDs:", role_ids)

    user = user_datastore.create_user(**data)
    db.session.flush()  # Assigns an ID to user

    if role_ids:
        roles = Role.query.filter(Role.id.in_(role_ids)).all()
        print("Fetched roles:", roles)
        user.roles = roles
        print("User after assigning roles:", user)

    db.session.commit()
    return user




class UserApi(BaseApi):
    model = User
    schema = UserSchema(load_instance=False)

    # def post(self):
    #     data = self.schema.load(request.json)
    #     user = user_datastore.create_user(**data)
    #     db.session.commit()
    #     return self.schema.dump(user), 201
    
  
    
    def post(self):
        data = self.schema.load(request.json)
        print(data)

        role_ids = data.pop('roles', [])
        print(role_ids)

        # Create user without roles
        user = user_datastore.create_user(**data)
        db.session.flush()  # Assigns an ID to user

        # Assign roles
        if role_ids:
            roles = Role.query.filter(Role.id.in_(role_ids)).all()
            user.roles = roles

        db.session.commit()
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