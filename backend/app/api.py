from flask import Blueprint, request
from flask_restful import Resource, Api
from .models import db, User, Book, Genre, Author, Member, user_datastore
from .schemas import (
    user_schema,
    users_schema,
    member_schema,
    members_schema,
    BookSchema,
    GenreSchema,
    AuthorSchema
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
    

class UserListApi(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        data = user_schema.load(request.json)
        user = user_datastore.create_user(**data)
        db.session.commit()
        return user_schema.dump(user), 201


class UserApi(Resource):
    def get(self, user_id):
        user = user_datastore.find_user(id=user_id)
        if not user:
            return {"message": "User not found"}, 404
        return user_schema.dump(user)

    def put(self, user_id):
        user = user_datastore.find_user(id=user_id)
        if not user:
            return {"message": "User not found"}, 404
        updated_data = user_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user_schema.dump(user)

    def delete(self, user_id):
        user = user_datastore.find_user(id=user_id)
        if not user:
            return {"message": "User not found"}, 404
        user_datastore.delete_user(user)
        db.session.commit()
        return {"message": "User deleted successfully."}


class MemberListApi(Resource):
    def get(self):
        members = Member.query.all()
        return members_schema.dump(members)

    def post(self):
        data = member_schema.load(request.json)
        member = user_datastore.create_user(**data, roles=["member"])
        db.session.commit()
        return member_schema.dump(member), 201


class MemberApi(Resource):
    def get(self, member_id):
        member = user_datastore.find_user(id=member_id)
        if not member:
            return {"message": "Member not found"}, 404
        return member_schema.dump(member)

    def put(self, member_id):
        member = user_datastore.find_user(id=member_id)
        if not member:
            return {"message": "Member not found"}, 404
        updated_data = member_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(member, key, value)
        db.session.commit()
        return member_schema.dump(member)

    def delete(self, member_id):
        member = user_datastore.find_user(id=member_id)
        if not member:
            return {"message": "Member not found"}, 404
        user_datastore.delete_user(member)
        db.session.commit()
        return {"message": "Member deleted successfully."}



def add_resource_routes(api, resource_api_class, endpoint_name, id_type='int'):
    api.add_resource(resource_api_class, f'/api/{endpoint_name}', endpoint=f'{endpoint_name}_list')
    api.add_resource(resource_api_class, f'/api/{endpoint_name}/<{id_type}:id>', endpoint=f'{endpoint_name}')
    
# Add routes for BookApi, GenreApi, AuthorApi, etc.
add_resource_routes(api, BookApi, 'books')
add_resource_routes(api, GenreApi, 'genres')
add_resource_routes(api, AuthorApi, 'authors')    


api.add_resource(UserListApi, "/api/users")
api.add_resource(UserApi, "/api/users/<int:user_id>")
api.add_resource(MemberListApi, "/api/members")
api.add_resource(MemberApi, "/api/members/<int:member_id>")
