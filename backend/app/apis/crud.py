from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import desc, or_
from urllib.parse import parse_qs
from app.models import (
    db,
    user_datastore,
    User,
    Book,
    Genre,
    Author,
    Member,
    Librarian,
    BookLoan
)
from app.schemas import (
    BookSchema,
    GenreSchema,
    AuthorSchema,
    UserSchema,
    MemberSchema,
    LibrarianSchema,
    BookLoanSchema
)
# from flask_security import login_required

crud_api_bp = Blueprint("crud_api_bp", __name__)
crud_api = Api(crud_api_bp)


class BaseApi(Resource):
    model = None
    schema = None

    def get(self, id=None):
        if id:
            obj = self.model.query.get_or_404(id)
            return self.schema.dump(obj)
        else:
            query = self.model.query
            query = self.apply_filters(query)
            query = self.apply_sorting(query)
            objs = query.all()
            return self.schema.dump(objs, many=True)

    def apply_filters(self, query):
        for key in request.args:
            if key.startswith('filters['):
                # Extracting the actual filter key from 'filters[<key>]'
                filter_key = key[8:-1]  # Removes 'filters[' and ']'
                if hasattr(self.model, filter_key):
                    filter_value = request.args[key]
                    query = query.filter(getattr(self.model, filter_key) == filter_value)
        return query

        for key in request.args:
            if key.startswith('filters['):
                filter_key = key[8:-1]  # Removes 'filters[' and ']'
                filter_value = request.args[key]
                
                if '__' in filter_key:
                    # Handle relationships (e.g., 'genres__name')
                    relationship, field = filter_key.split('__')
                    if hasattr(self.model, relationship):
                        related_model = getattr(self.model, relationship).property.mapper.class_
                        if hasattr(related_model, field):
                            query = query.join(related_model).filter(getattr(related_model, field) == filter_value)
                elif filter_key.endswith('__in'):
                    # Handle 'in' conditions (e.g., 'id__in')
                    actual_key = filter_key[:-4]
                    if hasattr(self.model, actual_key):
                        filter_values = filter_value.split(',')
                        query = query.filter(getattr(self.model, actual_key).in_(filter_values))
                elif filter_key.endswith('__contains'):
                    # Handle 'contains' conditions (e.g., 'title__contains')
                    actual_key = filter_key[:-10]
                    if hasattr(self.model, actual_key):
                        query = query.filter(getattr(self.model, actual_key).contains(filter_value))
                else:
                    # Handle simple equality conditions
                    if hasattr(self.model, filter_key):
                        query = query.filter(getattr(self.model, filter_key) == filter_value)
        
        return query    


        for key in request.args:
            if key.startswith('filters['):
                filter_key = key[8:-1]  # Removes 'filters[' and ']'
                filter_value = request.args[key]
                
                if '__' in filter_key:
                    # Handle relationships (e.g., 'genres__name')
                    relationship, field = filter_key.split('__')
                    if hasattr(self.model, relationship):
                        related_model = getattr(self.model, relationship).mapper.class_
                        if hasattr(related_model, field):
                            query = query.join(related_model).filter(getattr(related_model, field) == filter_value)
                elif filter_key.endswith('__in'):
                    # Handle 'in' conditions (e.g., 'id__in')
                    actual_key = filter_key[:-4]
                    if hasattr(self.model, actual_key):
                        filter_values = filter_value.split(',')
                        query = query.filter(getattr(self.model, actual_key).in_(filter_values))
                elif filter_key.endswith('__contains'):
                    # Handle 'contains' conditions (e.g., 'title__contains')
                    actual_key = filter_key[:-10]
                    if hasattr(self.model, actual_key):
                        query = query.filter(getattr(self.model, actual_key).contains(filter_value))
                else:
                    # Handle simple equality conditions
                    if hasattr(self.model, filter_key):
                        query = query.filter(getattr(self.model, filter_key) == filter_value)
        
        return query
    def apply_sorting(self, query):
        sort_by = request.args.get('sort_by')
        sort_order = request.args.get('sort_order', 'asc')

        if sort_by and hasattr(self.model, sort_by):
            sort_column = getattr(self.model, sort_by)
            if sort_order == 'desc':
                query = query.order_by(desc(sort_column))
            else:
                query = query.order_by(sort_column)
        return query

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

class BookLoanApi(BaseApi):
    model = BookLoan
    schema = BookLoanSchema()    


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
add_resource_routes(crud_api, BookApi, "books")
add_resource_routes(crud_api, GenreApi, "genres")
add_resource_routes(crud_api, AuthorApi, "authors")
add_resource_routes(crud_api, UserApi, "users")
add_resource_routes(crud_api, MemberApi, "members")
add_resource_routes(crud_api, LibrarianApi, "librarians")
add_resource_routes(crud_api, BookLoanApi, "bookloans")