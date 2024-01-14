from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, SelectMultipleField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email

# class SelectMultipleField(SelectMultipleField):
#     def process_formdata(self, valuelist):
#         self.data = [int(x) for x in valuelist]



class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    isbn_13 = StringField('ISBN-13')
    isbn_10 = StringField('ISBN-10')
    publisher = StringField('Publisher')
    publication_date = DateField('Publication Date')  # Use StringField for simplicity
    language = StringField('Language')
    content = TextAreaField('Content')
    submit = SubmitField('Submit')
    
class AuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()])
    submit = SubmitField('Submit')    
    
class GenreForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')    

class CreateUserForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EditUserForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    middle_name = StringField("Middle Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    username = StringField("User Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    contact = StringField("Contact", validators=[DataRequired()])
    gender = SelectField(
        "Gender", choices=[("male", "Male"), ("female", "Female"), ("other", "Other")]
    )
    dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    category = SelectField(
        "Category",
        choices=[("general", "General"), ("sebc", "SEBC"), ("sc", "SC"), ("st", "ST")],
    )
    blood_group = SelectField(
        "Blood Group",
        choices=[
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("AB+", "AB+"),
            ("AB-", "AB-"),
            ("O+", "O+"),
            ("O-", "O-"),
        ])

    roles = SelectMultipleField(
        "Roles",
        choices=[("admin", "Admin"), ("student", "Student"), ("faculty", "Faculty"), ("la", "Lab Assistant"), ("principal", "Principal"), ("hod", "HOD")],
    )

    submit = SubmitField("Submit")