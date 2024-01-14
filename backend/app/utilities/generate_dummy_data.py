import random
from faker import Faker
from app.extensions import db
from datetime import datetime, timedelta
from flask_security import UserMixin, RoleMixin, hash_password
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import *

def generate_dummy_data():
    print("Generating dummy data...")
    fake = Faker()

    # Create roles if they don't exist
    student_role = Role.query.filter_by(name="student").first()
    if not student_role:
        student_role = Role(name="student", description="Student role")
        db.session.add(student_role)

    staff_role = Role.query.filter_by(name="staff").first()
    if not staff_role:
        staff_role = Role(name="staff", description="Staff role")
        db.session.add(staff_role)

    db.session.commit()

    # Create librarian if it doesn't exist
    librarian = Librarian.query.filter_by(username="librarian").first()
    if not librarian:
        librarian = Librarian(
            username="librarian",
            email="librarian@example.com",
            password=generate_password_hash("password"),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        db.session.add(librarian)

    db.session.commit()

    # Create User if there are less than 15
    user_count = User.query.count()
    if user_count < 15:
        for _ in range(15 - user_count):
            user_datastore.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=hash_password("password"),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )
        # for _ in range(15 - user_count):
        #     user = User(
        #         username=fake.user_name(),
        #         email=fake.email(),
        #         password=generate_password_hash("password"),
        #         first_name=fake.first_name(),
        #         last_name=fake.last_name(),
        #     )
        #     db.session.add(user)

    db.session.commit()

    # # Create students if there are less than 10
    # student_count = Student.query.count()
    # if student_count < 10:
    #     student_role = Role.query.filter_by(name="student").first()
    #     for _ in range(10 - student_count):
    #         student = Student(
    #             username=fake.user_name(),
    #             email=fake.email(),
    #             password=generate_password_hash("password"),
    #             first_name=fake.first_name(),
    #             last_name=fake.last_name(),
    #             enrollment_number=fake.random_int(min=1000, max=9999),
    #             branch=fake.random_element(elements=("Computer Science", "Electrical Engineering", "Mechanical Engineering")),
    #             admission_year=fake.random_int(min=2015, max=2020),
    #         )
    #         student.roles.append(student_role)
    #         db.session.add(student)

    # db.session.commit()

    # # Create staff if there are less than 5
    # staff_count = Staff.query.count()
    # if staff_count < 5:
    #     staff_role = Role.query.filter_by(name="staff").first()
    #     for _ in range(5 - staff_count):
    #         staff = Staff(
    #             username=fake.user_name(),
    #             email=fake.email(),
    #             password=generate_password_hash("password"),
    #             first_name=fake.first_name(),
    #             last_name=fake.last_name(),
    #             staff_id=fake.random_int(min=1000, max=9999),
    #             department=fake.random_element(elements=("HR", "Finance", "IT")),
    #             designation=fake.random_element(elements=("Manager", "Officer", "Executive")),
    #         )
    #         staff.roles.append(staff_role)
    #         db.session.add(staff)

    # db.session.commit()

    # Create authors if there are less than 10
    author_count = Author.query.count()
    if author_count < 10:
        for _ in range(10 - author_count):
            author = Author(
                name=fake.name(),
                description=fake.text(),
            )
            db.session.add(author)

    db.session.commit()

    # Create sections if there are less than 5
    section_count = Section.query.count()
    if section_count < 5:
        for _ in range(5 - section_count):
            section = Section(
                name=fake.word(),
                description=fake.text(),
                date_created=fake.date_time_between(start_date="-1y", end_date="now"),
            )
            db.session.add(section)
    db.session.commit()                

    # Create books
    book_count = Book.query.count()
    if book_count < 20:
        for _ in range(20 - book_count):
            authors = random.sample(Author.query.all(), k=fake.random_int(min=1, max=3))
            section = random.choice(Section.query.all())
            book = Book(
                title=fake.sentence(nb_words=4, variable_nb_words=True),
                content=fake.paragraph(nb_sentences=10, variable_nb_sentences=True),
                isbn=fake.isbn13(separator=""),
                publisher=fake.company(),
                publication_date=fake.date_between(start_date="-10y", end_date="now"),
                language=fake.language_code(),
                file_path=fake.file_path(depth=1),
                authors=authors,
                section=section,
            )
            db.session.add(section)
    db.session.commit()