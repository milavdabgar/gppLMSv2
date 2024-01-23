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