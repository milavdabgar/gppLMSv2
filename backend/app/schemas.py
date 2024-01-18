from app.extensions import ma
from marshmallow import fields
from marshmallow_sqlalchemy.fields import Nested
from .extensions import db

from .models import (
    Role,
    User,
    Librarian,
    Member,
    Membership,
    Wishlist,
    Collection,
    Genre,
    Author,
    Book,
    Transaction,
    BookLoan,
    Purchase,
    Review
)


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        sqla_session = db.session


# class UserSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = User
#         load_instance = True
#         exclude = ("fs_uniquifier",)

class UserSchema(ma.SQLAlchemyAutoSchema):
    roles = ma.Nested(RoleSchema, many=True, only=['id', 'name'])
    class Meta:
        model = User
        load_instance = False
        sqla_session = db.session
        exclude = ("fs_uniquifier", "password",)
        # include_fk = True


class LibrarianSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Librarian
        load_instance = True
        sqla_session = db.session


class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True
        sqla_session = db.session


class MembershipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Membership
        load_instance = True
        sqla_session = db.session


class WishlistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wishlist
        load_instance = True
        sqla_session = db.session


class CollectionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Collection
        load_instance = True
        sqla_session = db.session


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True
        sqla_session = db.session


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        sqla_session = db.session


class BookSchema(ma.SQLAlchemyAutoSchema):  
    authors = ma.Nested(AuthorSchema, many=True, only=['id', 'name'])
    genres = ma.Nested(GenreSchema, many=True, only=['id', 'name'])
    collections = ma.Nested(CollectionSchema, many=True) 
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session
        # include_fk = True
        



class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        load_instance = True
        sqla_session = db.session


class BookLoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookLoan
        load_instance = True
        sqla_session = db.session


class PurchaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Purchase
        load_instance = True
        sqla_session = db.session


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        sqla_session = db.session


role_schema = RoleSchema()
roles_schema = RoleSchema(many = True)

user_schema = UserSchema()
users_schema = UserSchema(many = True)

librarian_schema = LibrarianSchema()
librarians_schema = LibrarianSchema(many = True)

member_schema = MemberSchema()
members_schema = MemberSchema(many = True)

membership_schema = MembershipSchema()
memberships_schema = MembershipSchema(many = True)

wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many = True)

collections_schema = CollectionSchema()
collections_schema = CollectionSchema(many = True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

book_schema = BookSchema()
books_schema = BookSchema(many=True)

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

book_loan_schema = BookLoanSchema()
book_loans_schema = BookLoanSchema(many=True)

purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)