from flask import Blueprint, render_template, redirect, url_for
# from app.forms import RegistrationForm, ExtendedRegisterForm
from app.models import user_datastore, db

auth_bp = Blueprint("auth_bp", __name__)


# @auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     form = ExtendedRegisterForm()

#     if form.validate_on_submit():
#         # Create a new user with the form data
#         user_datastore.create_user(
#             email=form.email.data,
#             password=form.password.data,
#             first_name=form.first_name.data,
#             last_name=form.last_name.data
#             # Set other user attributes
#         )
#         db.session.commit()

#         # Redirect to the login page or any other page as needed
#         return redirect(url_for('security.login'))

#     return render_template('security/register_user.html', form=form)


# @auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         # Here you can create a new user with the form data
#         email = form.email.data
#         password = form.password.data
#         user_datastore.create_user(email=email, password=password)
#         db.session.commit()
#         # Redirect to the login page or wherever you want
#         return redirect(url_for('index'))
#     return render_template('security/register_user.html', form=form)

# @auth_bp.route('/register')
# def register():
#     return render_template('security/register_user.html', register_user_form=ExtendedRegisterForm())

# @auth_bp.route('/login')
# def login():
#     return render_template('security/login_user.html', login_user_form=ExtendedLoginForm())