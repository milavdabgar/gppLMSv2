from app.extensions import ma
from marshmallow import fields
from marshmallow_sqlalchemy.fields import Nested

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


class UserSchema(ma.SQLAlchemyAutoSchema):
    # roles = Nested(RoleSchema, many=True)  # many=True for many-to-many relationship
    # Assuming roles are just a list of role IDs
    roles = fields.List(fields.Integer())

    class Meta:
        model = User
        load_instance = True  # Set this according to your use case
        # include_fk = True  # Include foreign keys if necessary
        exclude = ("fs_uniquifier",)  # Exclude fields as needed


class LibrarianSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Librarian
        load_instance = True


class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True


class MembershipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Membership
        load_instance = True


class WishlistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wishlist
        load_instance = True


class CollectionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Collection
        load_instance = True


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        load_instance = True


class BookLoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookLoan
        load_instance = True


class PurchaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Purchase
        load_instance = True


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True


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