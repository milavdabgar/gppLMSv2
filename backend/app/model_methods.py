from app.extensions import db, login
from datetime import datetime, timedelta
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


# Association table for many-to-many relationship between roles and users
roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)


class Role(db.Model, RoleMixin, CRUDMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin, CRUDMixin):
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



class Librarian(User):
    __mapper_args__ = {"polymorphic_identity": "librarian"}



class Member(User):
    __mapper_args__ = {"polymorphic_identity": "member"}
    max_books_allowed = db.Column(db.Integer, default=5)
    borrowed_books = db.relationship("BorrowedBook", backref="member", lazy="dynamic")
    reviews = db.relationship("Review", backref="member", lazy="dynamic")

    def view_sections(self):
        return Section.query.all()

    def view_books(self):
        return Book.query.all()

    def has_borrowed_book(self, book):
        return (
            self.borrowed_books.filter_by(book_id=book.id, status="borrowed").first()
            is not None
        )

    def can_borrow_more(self):
        return (
            self.borrowed_books.filter_by(status="borrowed").count()
            < self.max_books_allowed
        )

    def borrow_book(self, book):
        if not self.can_borrow_more():
            raise Exception("Borrowing limit reached")
        if self.has_borrowed_book(book):
            raise Exception("Book already borrowed")

        borrowed_book = BorrowedBook(member_id=self.id, book_id=book.id)
        db.session.add(borrowed_book)
        db.session.commit()

    def return_book(self, book):
        borrowed_book = self.borrowed_books.filter_by(
            book_id=book.id, status="borrowed"
        ).first()
        if borrowed_book:
            borrowed_book.returned_date = datetime.utcnow()
            borrowed_book.status = "returned"
            db.session.commit()
        else:
            raise Exception("Book not borrowed")

    def get_overdue_books(self):
        return self.borrowed_books.filter(
            BorrowedBook.due_date < datetime.utcnow(), BorrowedBook.status == "borrowed"
        ).all()

    def calculate_total_fine(self):
        overdue_books = self.get_overdue_books()
        total_fine = sum(book.calculate_fine() for book in overdue_books)
        return total_fine

    def get_borrowed_books(self):
        return self.borrowed_books.filter_by(status="borrowed").all()

    def write_review(self, book, rating, review_text):
        review = Review(
            member_id=self.id, book_id=book.id, rating=rating, review=review_text
        )
        db.session.add(review)
        db.session.commit()


class Staff(Member):
    __mapper_args__ = {"polymorphic_identity": "staff"}
    staff_id = db.Column(db.String(100))
    department = db.Column(db.String(100))
    designation = db.Column(db.String(100))


class Student(Member):
    __mapper_args__ = {"polymorphic_identity": "student"}
    enrollment_number = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    admission_year = db.Column(db.String(100))


class Principal(Staff):
    __mapper_args__ = {"polymorphic_identity": "principal"}


class HOD(Staff):
    __mapper_args__ = {"polymorphic_identity": "hod"}


class Lecturer(Staff):
    __mapper_args__ = {"polymorphic_identity": "lecturer"}


class LabAssistant(Staff):
    __mapper_args__ = {"polymorphic_identity": "lab_assistant"}


class Peon(Staff):
    __mapper_args__ = {"polymorphic_identity": "peon"}


# Association table for many-to-many relationship between authors and books
authors_books = db.Table(
    "authors_books",
    db.Column("book_id", db.Integer(), db.ForeignKey("book.id")),
    db.Column("author_id", db.Integer(), db.ForeignKey("author.id")),
)



class Author(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)


class Section(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    books = db.relationship("Book", backref="section", lazy="dynamic")

    def update_section(self, name=None, description=None):
        if name:
            self.name = name
        if description:
            self.description = description
        db.session.commit()


class Book(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)  # Use appropriate storage for book content
    isbn = db.Column(db.String(13))  # ISBN-13
    publisher = db.Column(db.String(100))
    publication_date = db.Column(db.Date)
    language = db.Column(db.String(50))
    no_of_pages = db.Column(db.Integer)
    file_path = db.Column(db.String(255))  # Path to the book file
    authors = db.relationship(
        "Author", secondary=authors_books, backref=db.backref("books", lazy="dynamic")
    )
    section_id = db.Column(db.Integer, db.ForeignKey("section.id"))
    borrowed_books = db.relationship("BorrowedBook", backref="book", lazy="dynamic")
    reviews = db.relationship("Review", backref="book", lazy="dynamic")

    def average_rating(self):
        total_rating = sum(review.rating for review in self.reviews)
        total_reviews = self.reviews.count()
        return total_rating / total_reviews if total_reviews > 0 else 0

    def assign_to_section(self, section_id):
        self.section_id = section_id
        db.session.commit()


class BorrowedBook(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(
        db.DateTime, default=datetime.utcnow() + timedelta(days=7)
    )  # Default borrowing duration
    returned_date = db.Column(db.DateTime)
    status = db.Column(
        db.String(20), default="borrowed"
    )  # 'borrowed', 'returned', 'overdue'
    fine = db.Column(db.Float, default=0.0)

    def check_overdue(self):
        return datetime.utcnow() > self.due_date

    def calculate_fine(self):
        if self.check_overdue():
            overdue_days = (datetime.utcnow() - self.due_date).days
            return overdue_days * 0.5  # Fine of $0.50 per day
        else:
            return 0.0


class Review(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)  # e.g., 1-5
    review = db.Column(db.Text)
    member_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
