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
from wtforms.validators import DataRequired, Email
from .models import Role

# class SelectMultipleField(SelectMultipleField):
#     def process_formdata(self, valuelist):
#         self.data = [int(x) for x in valuelist]


class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    isbn_13 = StringField("ISBN-13")
    isbn_10 = StringField("ISBN-10")
    publisher = StringField("Publisher")
    publication_date = DateField("Publication Date")  # Use StringField for simplicity
    language = StringField("Language")
    content = TextAreaField("Content")
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
    roles = SelectMultipleField("Roles", coerce=int)
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.type.choices = [(role.name.lower(),role.name) for role in Role.query.all()]
        self.roles.choices = [(str(role.id), role.name) for role in Role.query.all()]

    

class CreateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    roles = SelectMultipleField("Roles", coerce=int)
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.roles.choices = [(role.id, role.name) for role in Role.query.all()]
