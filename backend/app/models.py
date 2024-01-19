from app.extensions import db
from datetime import datetime, timedelta
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore


class CRUDMixin(db.Model):
    """
    Mixin that adds convenience methods for CRUD
    (create, read, update, delete) operations.
    """

    __abstract__ = True  # declares this as an abstract class

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()

    # Optional: Implement a method to serialize data, useful for APIs
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# Association tables for many-to-many relationships
roles_users = db.Table(
    "roles_users",
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
)

member_books = db.Table(
    "member_books",
    db.Column("member_id", db.Integer(), db.ForeignKey("member.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)


membership_books = db.Table(
    "membership_books",
    db.Column("membership_id", db.Integer(), db.ForeignKey("membership.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

wishlist_books = db.Table(
    "wishlist_books",
    db.Column("wishlist_id", db.Integer(), db.ForeignKey("wishlist.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

collection_books = db.Table(
    "collection_books",
    db.Column("collection_id", db.Integer(), db.ForeignKey("collection.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

authors_books = db.Table(
    "authors_books",
    db.Column("author_id", db.Integer(), db.ForeignKey("author.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)

genres_books = db.Table(
    "genres_books",
    db.Column("genre_id", db.Integer(), db.ForeignKey("genre.id")),
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
)


class Role(RoleMixin, CRUDMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(UserMixin, CRUDMixin):
    __mapper_args__ = {"polymorphic_identity": "user", "polymorphic_on": "type"}
    id = db.Column(db.Integer, primary_key=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    roles = db.relationship(
        "Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic")
    )
    type = db.Column(db.String(50))


class Admin(User):
    __mapper_args__ = {"polymorphic_identity": "admin"}
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)


class Librarian(User):
    __mapper_args__ = {"polymorphic_identity": "librarian"}
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)


class Member(User):
    __mapper_args__ = {"polymorphic_identity": "member"}
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    membership_id = db.Column(db.Integer, db.ForeignKey("membership.id"))
    preferred_genres = db.Column(db.String(255))  # Store comma-separated genre IDs
    language_preference = db.Column(db.String(50))
    # Relationships
    reading_history = db.relationship(
        "Book", secondary=member_books, backref="member", lazy="dynamic"
    )
    transactions = db.relationship("Transaction", backref="member", lazy="dynamic")
    book_loans = db.relationship("BookLoan", backref="member", lazy="dynamic")
    purchases = db.relationship("Purchase", backref="member", lazy="dynamic")
    wishlists = db.relationship("Wishlist", backref="member", lazy="dynamic")
    collections = db.relationship("Collection", backref="member", lazy="dynamic")
    reviews = db.relationship("Review", backref="member", lazy="dynamic")


class Membership(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))  # Silver, Gold, Platinum
    price = db.Column(db.Float)
    duration_type = db.Column(db.String(50))  # monthly, yearly, lifetime
    max_books_allowed = db.Column(db.Integer)
    discount_rate = db.Column(db.Float)  # Discount on purchases
    members = db.relationship("Member", backref="membership", lazy="dynamic")


class Wishlist(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Collection(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Genre(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)


class Author(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String, nullable=False)


class Book(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)  # Use appropriate storage for book content
    isbn_13 = db.Column(db.String(13))  # ISBN-13
    isbn_10 = db.Column(db.String(10))  # ISBN-10
    publisher = db.Column(db.String(100))
    publication_date = db.Column(db.Date)
    language = db.Column(db.String(50))
    type = db.Column(db.String(50))  # Physical, eBook, Audiobook

    # Relationships: Many to Many
    authors = db.relationship(
        "Author", secondary=authors_books, backref="books", lazy="dynamic"
    )
    genres = db.relationship(
        "Genre", secondary=genres_books, backref="books", lazy="dynamic"
    )
    collections = db.relationship(
        "Collection", secondary=collection_books, backref="books", lazy="dynamic"
    )
    wishlists = db.relationship(
        "Wishlist", secondary=wishlist_books, backref="book", lazy="dynamic"
    )
    free_access_in_memberships = db.relationship(
        "Membership", secondary=membership_books, backref="book", lazy="dynamic"
    )
    # Relationships: One to Many
    transactions = db.relationship("Transaction", backref="book", lazy="dynamic")
    book_loans = db.relationship("BookLoan", backref="book", lazy="dynamic")
    purchases = db.relationship("Purchase", backref="book", lazy="dynamic")
    reviews = db.relationship("Review", backref="book", lazy="dynamic")


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    type = db.Column(db.String(20))  # 'Loan', 'purchase' etc.
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20))  # 'active', 'completed'


class BookLoan(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(
        db.DateTime, default=lambda: datetime.utcnow() + timedelta(days=14)
    )
    returned_date = db.Column(db.DateTime)
    status = db.Column(
        db.String(20), default="issued"
    )  # Statuses like requested, issued, overdue, returned
    fine = db.Column(db.Float, default=0.0)
    renewal_count = db.Column(db.Integer, default=0)


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    price = db.Column(db.Float)
    price_after_discount = db.Column(db.Float)


class Review(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)  # e.g., 1-5
    review = db.Column(db.Text)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
