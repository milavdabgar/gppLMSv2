from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    BooleanField,
    SelectField,
    SelectMultipleField,
    DateField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Email

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
    type = SelectField(
        "User Type",
        choices=[("admin", "Admin"), ("librarian", "Librarian"), ("member", "Member")],
    )
    roles = SelectMultipleField(
        "Roles",
        choices=[("admin", "Admin"), ("librarian", "Librarian"), ("member", "Member")],
    )
    submit = SubmitField("Submit")