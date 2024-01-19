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
from .models import Role, Author
from flask_security import RegisterForm, LoginForm


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

class RoleSelectForm(FlaskForm):
    roles = QuerySelectField(
        "Roles", query_factory=lambda: Role.query.all(), get_label="name"
    )
    submit = SubmitField("Submit")


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("User Name", validators=[DataRequired()])


class ExtendedLoginForm(LoginForm):
    username = StringField("User Name", validators=[DataRequired()])
