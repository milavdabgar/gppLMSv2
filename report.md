# Library Management System v2

## Project Requirements

Here's a structured project guideline for the Library Management System:

1. User Authentication and Authorization
   - Implement user registration and login functionality using Flask Security or JWT-based token authentication
   - Use Role-Based Access Control (RBAC) to differentiate between librarian and general users
   - Only one librarian account should exist in the system

2. General User Functionalities
   - View all existing sections and e-books
   - Request and return e-books (maximum of 5 e-books per user)
   - Access e-books for a specific period (e.g., 7 days) with automatic revocation after the period ends
   - Provide feedback for an e-book

3. Librarian Functionalities
   - Issue and revoke access to e-books for users
   - Edit existing sections and e-books (content, author name, pages/volume, etc.)
   - Remove sections and e-books
   - Assign books to sections
   - Monitor the current status of each e-book and the user it is issued to
   - View available e-books in the library

4. Search Functionality
   - Implement search functionality for sections and e-books based on section, author, etc.

5. Backend Jobs
   - Implement export, reporting, and alert jobs
   - Daily Reminder Job: Check if users have visited the app and send alerts via Google Chat webhook, SMS, or email
   - Monthly Activity Report Job: Generate a monthly progress report in HTML or PDF format and send it to users via email

6. Backend Performance
   - Optimize backend performance for efficient handling of requests and data processing

7. Core Features
   - Librarian Dashboard: Provide an overview of the library system for the librarian
   - General User Profile: Allow users to view and update their profile information
   - Section Management: Enable the librarian to add, edit, and remove sections
   - E-book Management: Allow the librarian to add, edit, and remove e-books

8. Recommended Features (Optional)
   - Download e-books as PDF for a price
   - APIs for interaction with sections and books (CRUD operations)
   - Additional APIs for generating graphs for the librarian dashboard
   - Form validation for all input fields with suitable messages
   - Backend validation before storing or retrieving data from the database

9. Optional Features
   - Styling and aesthetics to enhance the user interface
   - Proper login system with additional security measures
   - Subscription or paid versions of the app with additional features (e.g., become an author)
   - Text-to-speech functionality for reading e-books to users

10. Storage and Encoding
    - Ensure the storage system handles multiple languages (UTF-8 encoding is usually sufficient)

11. Documentation and Deployment
    - Prepare comprehensive documentation for the system, including user guides and technical documentation
    - Deploy the Library Management System on a suitable hosting platform

Remember to follow best practices for software development, including version control, testing, and code organization. Use appropriate frameworks and libraries to streamline the development process and ensure a robust and scalable system.

## Directory Tree (codeTree.md)

```shell
.
├── backend
│   ├── api-ideas copy.md
│   ├── api-ideas.md
│   ├── app
│   │   ├── apis
│   │   │   ├── crud.py
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   ├── extensions.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes
│   │   │   ├── auth.py
│   │   │   ├── crud_api_calls.py
│   │   │   ├── __init__.py
│   │   │   ├── librarian.py
│   │   │   ├── main.py
│   │   │   └── member.py
│   │   ├── schemas.py
│   │   ├── services.py
│   │   ├── templates
│   │   │   ├── admin
│   │   │   │   └── index.html
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   ├── librarian
│   │   │   │   ├── edit.html
│   │   │   │   ├── home.html
│   │   │   │   ├── list.html
│   │   │   │   ├── user_add.html
│   │   │   │   ├── user_delete.html
│   │   │   │   ├── user_edit.html
│   │   │   │   ├── user_list.html
│   │   │   │   └── user_view.html
│   │   │   ├── main
│   │   │   │   └── select_role.html
│   │   │   ├── member
│   │   │   │   ├── books.html
│   │   │   │   ├── browse_books.html
│   │   │   │   ├── browse_genres.html
│   │   │   │   ├── home.html
│   │   │   │   └── loans.html
│   │   │   └── security
│   │   │       ├── base.html
│   │   │       ├── change_password.html
│   │   │       ├── email
│   │   │       │   ├── confirmation_instructions.html
│   │   │       │   ├── reset_instructions.html
│   │   │       │   ├── reset_notice.html
│   │   │       │   └── welcome.html
│   │   │       ├── forgot_password.html
│   │   │       ├── login_user.html
│   │   │       ├── register_user.html
│   │   │       └── reset_password.html
│   │   ├── utilities
│   │   │   ├── cached_data_clearer.py
│   │   │   ├── csvImports-standard.py
│   │   │   ├── database_utils.py
│   │   │   ├── excel_formatter.py
│   │   │   ├── generate_dummy_data.py
│   │   │   ├── image_uploader.py
│   │   │   ├── lesson_planner.py
│   │   │   ├── pdf_weasyprint.py
│   │   │   ├── search.py
│   │   │   ├── term_dates_generator.py
│   │   │   ├── topic_extractor.py
│   │   │   └── utils.py
│   │   └── views.py
│   ├── bookloan_api.md
│   ├── config.py
│   ├── db_migrator.sh
│   ├── GPPPortal.sqlite
│   ├── local_gunicorn.sh
│   ├── local_mailhog.sh
│   ├── local_run.sh
│   ├── local_setup.sh
│   ├── local_testing.sh
│   ├── main.py
│   ├── project-requirements.md
│   └── requirements.txt
├── codeTree.md
├── frontend
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── output.txt
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── README.md
│   ├── src
│   │   ├── App.vue
│   │   ├── assets
│   │   │   └── logo.png
│   │   ├── axiosConfig.js
│   │   ├── components
│   │   │   ├── auth
│   │   │   │   ├── ChangePassword.vue
│   │   │   │   ├── ForgotPassword.vue
│   │   │   │   ├── ProfileComponent.vue
│   │   │   │   ├── UserLogin.vue
│   │   │   │   ├── UserLogout.vue
│   │   │   │   └── UserRegistration.vue
│   │   │   ├── BookLoanDetailsComponent.vue
│   │   │   ├── BookLoanRequestComponent.vue
│   │   │   ├── BookLoanRequestsListComponent.vue
│   │   │   ├── BookLoansListComponent.vue
│   │   │   ├── BrowseBooks.vue
│   │   │   ├── BrowseGenres.vue
│   │   │   ├── GeneralEdit.vue
│   │   │   ├── GeneralList.vue
│   │   │   └── RoleSelectionComponent.vue
│   │   ├── main.js
│   │   ├── router
│   │   │   └── index.js
│   │   ├── services
│   │   │   ├── BookLoanService.js
│   │   │   └── BookService.js
│   │   ├── store.js
│   │   └── views
│   │       ├── AboutView.vue
│   │       ├── HomeView.vue
│   │       ├── LibrarianDashboardView.vue
│   │       ├── MemberDashboardView.vue
│   │       └── MyLoansView.vue
│   └── vue.config.js
├── Library Management System.pdf
├── Library Management System-v2_ MAD - II.pdf
├── report.md
└── ToDo.md

21 directories, 111 files

```

### gppLMSv2/backend/requirements.txt

This file lists the required Python packages and their versions for the backend of the Library Management System. It includes packages such as Flask, Flask-RESTful, Flask-Security-Too, Flask-SQLAlchemy, and others that are necessary for building the application.

```
Flask
Flask-RESTful
Flask-Security-Too
Flask-SQLAlchemy
Flask-Mail
Flask-Migrate
flask-marshmallow
Flask-WTF
WTForms-SQLAlchemy
Flask-Bootstrap
python-dotenv
djlint
marshmallow_sqlalchemy
Flask-Admin
Flask-Babel
Flask-Cors
requests
faker
```

### gppLMSv2/backend/main.py

This is the entry point of the Flask application. It creates an instance of the Flask app using the create_app() function from the app package and runs the application.

```python
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

### gppLMSv2/backend/config.py

This file contains the configuration classes for the Flask application. It defines the Config base class and the LocalDevelopmentConfig class for local development settings. The configuration includes settings for the database, mail server, security, and other application-specific settings.

```python
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    DEBUG = False
    TESTING = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.googlemail.com"
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 587)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") or 1
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "admin@email.com"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "password"


    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SECURITY_PASSWORD_HASH = os.environ.get("SECURITY_PASSWORD_HASH") or "bcrypt"
    SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT") or "super secret"
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = False
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_TOKEN_AUTHENTICATION_HEADER = None
    SECURITY_POST_LOGIN_VIEW = "/select_role"
    WTF_CSRF_ENABLED = False
    
    FLASK_ADMIN_SWATCH = "cerulean"

class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "GPPPortal.sqlite")

    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    # SECURITY_CONFIRMABLE = True
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    SECURITY_CHANGEABLE = True

```

### gppLMSv2/backend/app/\__init__py

This file is the entry point of the app package. It creates the Flask application, initializes extensions (such as the database, migration, security, and admin), and registers blueprints for different routes. It also sets up the user datastore and creates the necessary database tables.

```python
from flask import Flask
from config import LocalDevelopmentConfig
from .extensions import db, migrate, security, bootstrap, mail, ma, babel, cors
from .apis.crud import crud_api_bp
from .apis.main import api_bp
from .routes.crud_api_calls import api_call_bp
from .routes.main import main_bp
from .routes.librarian import librarian_bp
from .routes.member import member_bp
from .routes.auth import auth_bp
from .utilities.utils import initialize_db
from .utilities.generate_dummy_data import generate_dummy_data
# import flask_excel as excel
# from flask_sse import sse
from .views import setup_admin
from .models import user_datastore
from .forms import ExtendedRegisterForm


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.app_context().push()
    

    mail.init_app(app)
    bootstrap.init_app(app)
    security.init_app(app, user_datastore, register_form=ExtendedRegisterForm)
    app.user_datastore = user_datastore

    # cache.init_app(app)
    # excel.init_excel(app)
    # admin.init_app(app)
    # moment.init_app(app)
    # login.init_app(app)
    babel.init_app(app)
    cors.init_app(app)
    setup_admin(app)
    with app.app_context():
        db.create_all()
        # generate_dummy_data()
        # initialize_db(user_datastore)
        # import app.views

    # Register Blueprints
    # app.register_blueprint(user_api_bp, user_datastore=user_datastore)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(crud_api_bp)
    app.register_blueprint(api_call_bp)
    app.register_blueprint(member_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(librarian_bp)
    # app.register_blueprint(main_bp)

    # # This is for streaming
    # app.register_blueprint(sse, url_prefix="/stream")
    # cors.init_app(app)

    return app

```

### gppLMSv2/backend/app/extensions.py

This file defines the Flask extensions used in the application, such as SQLAlchemy for database management, Migrate for database migrations, Flask-Security for authentication and authorization, and others. These extensions are initialized without any specific Flask app instance.

```python
# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_security import Security
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_babel import Babel
from flask_cors import CORS

# Initialize extensions, but without any specific app bound to them.
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
mail = Mail()
security = Security()
ma = Marshmallow()
babel = Babel()
cors = CORS()
```

### gppLMSv2/backend/app/models.py

This file contains the database models for the Library Management System. It defines the CRUDMixin class for CRUD operations, and various models such as Role, User, Admin, Librarian, Member, Membership, Wishlist, Collection, Genre, Author, Book, BookLoan, Purchase, and Review. These models represent the entities in the system and their relationships.

```python
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
    language_preference = db.Column(db.String(50))
    # Relationships
    reading_history = db.relationship(
        "Book", secondary=member_books, backref="member", lazy="dynamic"
    )
    book_loans = db.relationship("BookLoan", backref="member", lazy="dynamic")
    purchases = db.relationship("Purchase", backref="member", lazy="dynamic")
    wishlists = db.relationship("Wishlist", backref="member", lazy="dynamic")
    collections = db.relationship("Collection", backref="member", lazy="dynamic")
    reviews = db.relationship("Review", backref="member", lazy="dynamic")
    preferred_genres = db.relationship("Genre", backref="member", lazy="dynamic")


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
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))


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
    book_loans = db.relationship("BookLoan", backref="book", lazy="dynamic")
    purchases = db.relationship("Purchase", backref="book", lazy="dynamic")
    reviews = db.relationship("Review", backref="book", lazy="dynamic")


class BookLoan(CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    loan_date = db.Column(db.Date, default=datetime.utcnow().date())
    due_date = db.Column(
        db.Date, default=lambda: datetime.utcnow().date() + timedelta(days=14)
    )
    returned_date = db.Column(db.Date)
    status = db.Column(
        db.String(20), default="issued"
    )  # Statuses like requested, issued, overdue, returned


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

```

### gppLMSv2/backend/app/schemas.py

This file defines the Marshmallow schemas for serializing and deserializing the database models. It includes schemas for Role, User, Librarian, Member, Membership, Wishlist, Collection, Genre, Author, Book, BookLoan, Purchase, and Review. These schemas are used for data validation and conversion between JSON and Python objects.

```python
from app.extensions import ma
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
    BookLoan,
    Purchase,
    Review,
)


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        load_instance = True
        sqla_session = db.session


class UserSchema(ma.SQLAlchemyAutoSchema):
    roles = ma.Nested(RoleSchema, many=True, only=["id", "name"])

    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        exclude = (
            "fs_uniquifier",
            "password",
        )


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

class BookLoanSchema(ma.SQLAlchemyAutoSchema):
    # books = ma.Nested("BookSchema", only=["id", "title"])
    # member_id = ma.Nested("MemberSchema", only=["id", "email"])
    class Meta:
        model = BookLoan
        load_instance = True
        sqla_session = db.session
        include_fk = True

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

class BookSchema(ma.SQLAlchemyAutoSchema):
    authors = ma.Nested(AuthorSchema, many=True, only=["id", "name"])
    genres = ma.Nested(GenreSchema, many=True, only=["id", "name"])
    collections = ma.Nested(CollectionSchema, many=True)
    wishlists = ma.Nested(WishlistSchema, many=True)
    free_access_in_memberships = ma.Nested(MembershipSchema, many=True)
    book_loans = ma.Nested(BookLoanSchema, many=True)
    purchases = ma.Nested(PurchaseSchema, many=True)
    reviews = ma.Nested(ReviewSchema, many=True)

    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session

role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

librarian_schema = LibrarianSchema()
librarians_schema = LibrarianSchema(many=True)

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

membership_schema = MembershipSchema()
memberships_schema = MembershipSchema(many=True)

wishlist_schema = WishlistSchema()
wishlists_schema = WishlistSchema(many=True)

collections_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

book_schema = BookSchema()
books_schema = BookSchema(many=True)

book_loan_schema = BookLoanSchema()
book_loans_schema = BookLoanSchema(many=True)

purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

```

### gppLMSv2/backend/app/forms.py

This file contains the Flask-WTF form classes used in the application. It defines forms for managing books, authors, genres, users, members, and book loans. These forms include fields for inputting and validating data, and they are used in the routes for rendering HTML templates and handling form submissions.

```python
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    SelectField,
    SelectMultipleField,
    DateField,
    TextAreaField,
    PasswordField,
)
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo
from .models import Role, Author, Book, Member, User, Genre, db
from flask_security import RegisterForm


class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    isbn_13 = StringField("ISBN-13")
    isbn_10 = StringField("ISBN-10")
    publisher = StringField("Publisher")
    publication_date = DateField("Publication Date")  # Use StringField for simplicity
    language = StringField("Language")
    content = TextAreaField("Content")
    authors = QuerySelectMultipleField(
        "Authors", query_factory=lambda: Author.query.all(), get_label="name"
    )
    submit = SubmitField("Submit")


class AuthorForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    biography = StringField("Biography", validators=[DataRequired()])
    submit = SubmitField("Submit")


class GenreForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("User Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    type = SelectField("Type", coerce=str)
    roles = QuerySelectMultipleField(
        "Roles", query_factory=lambda: Role.query.all(), get_label="name"
    )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.type.choices = [
            (role.name.lower(), role.name) for role in Role.query.all()
        ]

class MemberForm(UserForm):
    preferred_genres = QuerySelectMultipleField(
        "Genre", query_factory=lambda: Genre.query.all(), get_label="name"
    )
    language_preference = StringField("Preferred Languages")
    # language_preference = SelectMultipleField(
    #     'Preferred Languages', 
    #     choices=[
    #         ('english', 'English'),
    #         ('hindi', 'Hindi'),
    #         ('gujarati', 'Gujarati'),
    #         ('others', 'Others')
    #     ],
    #     validators=[DataRequired()]
    # )

class RoleSelectForm(FlaskForm):
    roles = QuerySelectField(
        "Roles", query_factory=lambda: Role.query.all(), get_label="name"
    )
    submit = SubmitField("Submit")


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("User Name", validators=[DataRequired()])



class BookLoanForm(FlaskForm):
    book_id = QuerySelectField("Book", query_factory=lambda: Book.query.all(), get_label="title")
    member_id = QuerySelectField("Member", query_factory=lambda: Member.query.all(), get_label="email")
    # book_id = SelectField("Book", coerce=str) 
    # member_id = SelectField("Member", coerce=str)
    loan_date = DateField('Loan Date', validators=[DataRequired()])
    returned_date = DateField('Returned Date')
    status = SelectField(
        'Status', 
        choices=[
            ('requested', 'Requested'),
            ('approved', 'Approved'),
            ('active', 'Active'),
            ('overdue', 'Overdue'),
            ('returned', 'Returned')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit")

    # def __init__(self, *args, **kwargs):    
    #     super(BookLoanForm, self).__init__(*args, **kwargs)
    #     self.book_id.choices = [
    #         (book.id, book.title) for book in Book.query.all()
    #     ]
    #     self.member_id.choices = [
    #         (member.id, member.email) for member in Member.query.all()
    #     ]
```

### gppLMSv2/backend/app/apis/crud.py

This file defines the CRUD API endpoints using Flask-RESTful. It includes a BaseApi class that provides generic CRUD operations for database models, and specific API classes for User, Member, Librarian, Book, Genre, Author, and BookLoan. The API endpoints allow for retrieving, creating, updating, and deleting records, as well as filtering and sorting the results.

```python
from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import desc
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


# Base API class
# class BaseApi(Resource):
#     model = None
#     schema = None
#     def get(self, id=None):
#         if id:
#             obj = self.model.query.get_or_404(id)
#             return self.schema.dump(obj)
#         else:
#             objs = self.model.query.all()
#             return self.schema.dump(objs, many=True)

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
```

### gppLMSv2/backend/app/apis/main.py

This file defines the main API endpoints for the application. It includes endpoints for selecting user roles, retrieving book loans by member or book, approving loans, returning loans, and retrieving the currently logged-in user. These endpoints handle specific actions related to the library management system.

```python
from flask import Blueprint, jsonify, request, url_for
from flask_login import current_user
from flask_security import auth_required, login_required
from datetime import datetime
from ..models import db, BookLoan
from ..schemas import book_loan_schema, book_loans_schema, user_schema

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/api/select_role", methods=["GET", "POST"])
# @auth_required("token", "session")
@login_required
def select_role():
    data = request.json
    selected_role = data.get("role")
    if selected_role:
        if selected_role == "Librarian":
            return jsonify({"redirect_url": url_for("librarian_bp.home")})
        elif selected_role == "Member":
            return jsonify({"redirect_url": url_for("member_bp.home")})
    
    return jsonify({"error": "Invalid role selected"}), 400


# Get loans for a member
@api_bp.route("/api/bookloans/members/<int:member_id>", methods=['GET'])
def get_loans_by_member(member_id):
    loans = BookLoan.query.filter_by(member_id=member_id).all()
    return book_loans_schema.jsonify(loans)



# Get loans for a book
@api_bp.route("/api/bookloans/books/<int:book_id>", methods=['GET'])
def get_loans_by_book(book_id):
    loans = BookLoan.query.filter_by(book_id=book_id).all()
    return book_loans_schema.jsonify(loans)


# Approve loan
@api_bp.route("/api/bookloans/<int:loan_id>/approve", methods=["PUT"])
def approve_loan(loan_id):
    loan = BookLoan.query.get(loan_id)
    loan.status = "approved"
    db.session.commit()
    return book_loan_schema.jsonify(loan)


# Return loan
@api_bp.route("/api/bookloans/<int:loan_id>/return", methods=["PUT"])
def return_loan(loan_id):
    loan = BookLoan.query.get(loan_id)
    loan.returned_date = datetime.utcnow().date()
    loan.status = "returned"
    db.session.commit()
    return book_loan_schema.jsonify(loan)


@api_bp.route('/api/current_user', methods=['GET'])
@login_required
def get_current_user():
    return user_schema.jsonify(current_user)
```

### gppLMSv2/backend/app/routes/crud_api_calls.py

This file contains the routes for making API calls to the CRUD API endpoints. It defines routes for managing books, genres, authors, users, members, and book loans. These routes utilize forms for data input and validation, and they interact with the CRUD API endpoints to perform the corresponding operations.

```python
from flask import Blueprint, render_template, redirect, url_for
from ..forms import BookForm, GenreForm, AuthorForm, UserForm, BookLoanForm, MemberForm
from ..schemas import book_schema, genre_schema, author_schema, user_schema, book_loan_schema, member_schema
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
            print(serialized_data)
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

@api_call_bp.route("/members", methods=["GET", "POST"])
def member_list():
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=MemberForm,
        schema=member_schema,
        endpoint="members",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.member_list",
        list_title="Member List",
        edit_title="Edit Member",
        edit_route="api_call_bp.edit_member",
        display_fields=display_fields,
    )


# Edit member function
@api_call_bp.route("/members/<int:id>", methods=["GET", "POST"])
def edit_member(id):
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=MemberForm,
        schema=member_schema,
        endpoint="members",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.member_list",
        list_title=None,
        edit_title="Edit Member",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )


@api_call_bp.route("/bookloans", methods=["GET", "POST"])
def bookloan_list():
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=BookLoanForm,
        schema=book_loan_schema,
        endpoint="bookloans",
        template="librarian/list.html",
        redirect_endpoint="api_call_bp.bookloan_list",
        list_title="BookLoan List",
        edit_title="Edit BookLoan",
        edit_route="api_call_bp.edit_bookloan",
        display_fields=display_fields,
    )


# Edit BookLoan function
@api_call_bp.route("/bookloans/<int:id>", methods=["GET", "POST"])
def edit_bookloan(id):
    display_fields = [("email", "first_name")]
    return handle_form_submission(
        form_class=BookLoanForm,
        schema=book_loan_schema,
        endpoint="bookloans",
        template="librarian/edit.html",
        redirect_endpoint="api_call_bp.bookloan_list",
        list_title=None,
        edit_title="Edit BookLoan",
        edit_route=None,
        id=id,
        display_fields=display_fields,
    )

```

### gppLMSv2/backend/app/routes/librarian.py

This file defines the routes for the librarian functionality. It includes routes for the librarian dashboard, displaying users, adding users, editing users, and deleting users. These routes handle the librarian-specific actions and render the corresponding HTML templates.

```python
from flask import Blueprint
from flask import render_template, redirect, url_for
from flask_security import current_user
from ..forms import UserForm, BookForm
from ..models import db, user_datastore, User, Role
from ..services import create_book, get_all_books, get_book, update_book

librarian_bp = Blueprint("librarian_bp", __name__)


@librarian_bp.route("/librarian/home")
def home():
    return render_template("librarian/home.html")


@librarian_bp.route("/user/display")
def display_users():
    users = User.query.all()
    return render_template("librarian/user_list.html", users=users)


@librarian_bp.route("/user/show/<int:user_id>")
def show_user(user_id):
    user = user_datastore.find_user(id=user_id)
    if user:
        return render_template("librarian/user_view.html", user=user)
    return {"message": "User not found"}, 404


@librarian_bp.route("/user/add", methods=["GET", "POST"])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        # Create a new user with the basic fields
        data = {k: v for k, v in form.data.items() if k not in ["submit", "roles"]}
        user = user_datastore.create_user(**data)

        for role in form.roles.data:
            user.roles.append(role)

        # Commit the new user to the database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("librarian_bp.display_users"))

    return render_template("librarian/user_add.html", form=form)


@librarian_bp.route("/user/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("librarian_bp.display_users", user_id=user.id))

    # Pre-select the current roles in the form
    form.roles.data = [role for role in user.roles]

    return render_template("librarian/user_edit.html", form=form, user=user)


@librarian_bp.route("/user/delete/<int:user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("librarian_bp.display_users", user_id=user.id))
    return render_template("librarian/user_delete.html", user=user)
```

### gppLMSv2/backend/app/routes/main.py

This file contains the main routes for the application. It defines the routes for the home page and the role selection page. The role selection route is protected by authentication and handles the selection of user roles (librarian or member) based on the submitted form.

```python
from flask import Blueprint, render_template, url_for, redirect
from flask_security import auth_required
from ..forms import RoleSelectForm

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/select_role", methods=["GET", "POST"])
@auth_required("token", "session")
def select_role():
    form = RoleSelectForm()
    if form.validate_on_submit():
        selected_role = form.roles.data
        print(selected_role)
        if selected_role.name == "Librarian":
            return redirect(url_for("librarian_bp.home"))
        elif selected_role.name == "Member":
            return redirect(url_for("member_bp.home"))
    
    return render_template("main/select_role.html", form=form)
```

### gppLMSv2/backend/app/routes/member.py

This file defines the routes for the member functionality. It includes routes for the member dashboard, requesting a book, viewing loans, and returning a book. These routes handle the member-specific actions and interact with the API endpoints to perform the corresponding operations.

```python
from flask import Blueprint, render_template
from flask_security import auth_required
from ..models import Book
from ..routes.crud_api_calls import api_call

member_bp = Blueprint("member_bp", __name__)

@member_bp.route("/member/home")
@auth_required("token", "session")
def home():
    books = Book.query.all()
    return render_template("member/home.html", books=books)

def request_book(book_id, member_id):
    return api_call(f"books/request/{book_id}/{member_id}", method="post")


def view_loans(member_id):
    return api_call(f"loans/{member_id}", method="get")


def return_book(loan_id):
    return api_call(f"loans/return/{loan_id}", method="put")  
```

### gppLMSv2/frontend/src/main.js

This is the entry point of the Vue.js frontend application. It creates a new Vue instance, mounts the root component (App.vue), and initializes the router and store.

```javascript
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");

```



### gppLMSv2/frontend/src/store.js

This file defines the Vuex store for the frontend application. It includes the state, mutations, actions, and getters related to user authentication and management. The store handles user registration, login, logout, and fetching user data from the backend API.

```javascript
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
// import axiosInstance from './axiosConfig';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      paths: ["user"],
    }),
  ],

  state: {
    user: null,
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    SET_USER_ROLE(state, role) {
      if (state.user) {
        state.user.role = role;
      }
    },
    CLEAR_USER(state) {
      state.user = null;
    },
    CLEAR_USER_ROLE(state, role) {
      if (state.user) {
        state.user.role = role;
      }
    },
  },
  actions: {
    async register({ dispatch }, credentials) {
      try {
        const response = await axios.post(
          "http://localhost:5000/register",
          credentials,
          {
            params: {
              include_auth_token: true,
            },
          }
        );
        localStorage.setItem(
          "authToken",
          response.data.response.user.authentication_token
        );
        axios.defaults.headers.common["Authentication-Token"] =
          localStorage.authToken;
        await dispatch("fetchUser");
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
    async login({ dispatch }, credentials) {
      try {
        const response = await axios.post(
          "http://localhost:5000/login",
          credentials,
          {
            params: {
              include_auth_token: true,
            },
          }
        );
        localStorage.setItem(
          "authToken",
          response.data.response.user.authentication_token
        );
        axios.defaults.headers.common["Authentication-Token"] =
          localStorage.authToken;
        await dispatch("fetchUser");
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
    async fetchUser({ commit }) {
      const token = localStorage.getItem("authToken");
      if (token) {
        try {
          const userResponse = await axios.get(
            "http://localhost:5000/api/current_user"
          );
          commit("SET_USER", userResponse.data);
        } catch (error) {
          console.error("Error fetching user:", error);
        }
      }
    },

    async logout({ commit }) {
      try {
        await axios.post("http://localhost:5000/logout");
        localStorage.removeItem("authToken");
        axios.defaults.headers.common["Authentication-Token"] = "";
        commit("CLEAR_USER");
        commit("CLEAR_USER_ROLE");
      } catch (error) {
        console.error("Logout failed:", error);
      }
    },
  },

  getters: {
    userId(state) {
      return state.user.id;
    },
  },
});

```

### gppLMSv2/frontend/src/App.vue

This is the root component of the Vue.js application. It defines the main template structure, including the navigation menu and the router view component. It also includes styles for the application.

```vue
<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/librarian/home">LibrarianDashboardView</router-link> |
      <router-link to="/member/home">MemberDashboardView</router-link>
    </nav>
    <nav>
      <router-link to="/register">Register</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/logout">Logout</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

```

### gppLMSv2/frontend/src/router/index.js

This file defines the Vue Router configuration for the frontend application. It sets up the routes for different views and components, such as the home page, librarian dashboard, member dashboard, user authentication pages, and book/genre/author management pages.

```javascript
import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "@/views/HomeView.vue";
import MyLoansView from "@/views/MyLoansView.vue";
import LibrarianDashboardView from "@/views/LibrarianDashboardView.vue";
import MemberDashboardView from "@/views/MemberDashboardView.vue";

import UserRegistration from "@/components/auth/UserRegistration.vue";
import UserLogin from "@/components/auth/UserLogin.vue";
import UserLogout from "../components/auth/UserLogout.vue";
import ForgotPassword from "@/components/auth/ForgotPassword.vue";
import ChangePassword from "@/components/auth/ChangePassword.vue";

import RoleSelectionComponent from "@/components/RoleSelectionComponent.vue";
import BookLoanDetailsComponent from "@/components/BookLoanDetailsComponent.vue";

import BrowseBooks from "@/components/BrowseBooks.vue";
import BrowseGenres from "@/components/BrowseGenres.vue";
import GeneralList from "@/components/GeneralList.vue";
import GeneralEdit from "@/components/GeneralEdit.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/select-role",
    name: "SelectRole",
    component: RoleSelectionComponent,
  },

  {
    path: "/member/loans",
    name: "MyLoansView",
    component: MyLoansView,
  },

  {
    path: "/librarian/home",
    name: "LibrarianDashboardView",
    component: LibrarianDashboardView,
  },

  {
    path: "/member/home",
    name: "MemberDashboardView",
    component: MemberDashboardView,
  },
  {
    path: "/loan-details/:id",
    name: "LoanDetails",
    component: BookLoanDetailsComponent,
  },

  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },

  {
    path: "/login",
    name: "UserLogin",
    component: UserLogin,
  },
  {
    path: "/logout",
    name: "Logout",
    component: UserLogout,
  },
  {
    path: "/register",
    name: "UserRegister",
    component: UserRegistration,
  },
  {
    path: "/reset",
    name: "ForgotPassword",
    component: ForgotPassword,
  },
  {
    path: "/change",
    name: "ChangePassword",
    component: ChangePassword,
  },
  {
    path: "/browse-books",
    name: "BrowseBooks",
    component: BrowseBooks,
  },
  {
    path: "/browse-genres",
    name: "BrowseGenres",
    component: BrowseGenres,
  },

  {
    path: "/books/edit/:id",
    name: "EditBook",
    component: GeneralEdit,
    props: (route) => ({ type: "Book", id: route.params.id }),
  },

  {
    path: "/genres/edit/:id",
    name: "EditGenre",
    component: GeneralEdit,
    props: (route) => ({ type: "Genre", id: route.params.id }),
  },

  {
    path: "/authors/edit/:id",
    name: "EditAuthor",
    component: GeneralEdit,
    props: (route) => ({ type: "Author", id: route.params.id }),
  },

  {
    path: "/users/edit/:id",
    name: "EditUser",
    component: GeneralEdit,
    props: (route) => ({ type: "User", id: route.params.id }),
  },

  {
    path: "/books",
    component: GeneralList,
    props: {
      resourceType: "books",
      editRoute: "EditBook",
    },
  },

  {
    path: "/authors",
    component: GeneralList,
    props: {
      resourceType: "authors",
      editRoute: "EditAuthor",
    },
  },

  {
    path: "/genres",
    component: GeneralList,
    props: {
      resourceType: "genres",
      editRoute: "EditGenre",
    },
  },

  {
    path: "/users",
    component: GeneralList,
    props: {
      resourceType: "users",
      editRoute: "EditUser",
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;

```

### gppLMSv2/frontend/src/services/BookService.js

This file contains the BookService, which is responsible for making API requests related to books. It includes methods for creating, retrieving, updating, and deleting books using the corresponding API endpoints.

```javascript
import axios from "axios";

const API_URL = "http://localhost:5000/api/books";

export default {
  async createBook(book) {
    const response = await axios.post(API_URL, book);
    return response.data;
  },

  async getBooks(params = {}) {
    const response = await axios.get(API_URL, { params });
    return response.data;
  },

  async getBookById(id) {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  },

  async updateBook(id, book) {
    const response = await axios.put(`${API_URL}/${id}`, book);
    return response.data;
  },

  async deleteBook(id) {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data;
  },
};

```



### gppLMSv2/frontend/src/services/BookLoanService.js

This file contains the BookLoanService, which is responsible for making API requests related to book loans. It includes methods for creating, retrieving, updating, deleting, and approving book loans using the corresponding API endpoints.

```javascript
import axios from "axios";

const API_URL = "http://localhost:5000/api/bookloans";

export default {
  async createLoan(loan) {
    const response = await axios.post(API_URL, loan);
    return response.data;
  },

  // async getLoans(params = {}) {
  //   const response = await axios.get(API_URL, { params });
  //   return response.data;
  // },

  async getLoans(filters = {}, sort_by = {}, sort_order={}) {
    const queryParams = {
      filters: filters,
      sort_by: sort_by,
      sort_order: sort_order
    };
    const response = await axios.get(API_URL, { params: queryParams });
    return response.data;
  },
  

  async getLoanById(id) {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  },

  async updateLoan(id, loan) {
    const response = await axios.put(`${API_URL}/${id}`, loan);
    return response.data;
  },

  async deleteLoan(id) {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data;
  },

  async approveLoan(id) {
    const response = await axios.put(`${API_URL}/${id}/approve`);
    return response.data;
  },
};

```

