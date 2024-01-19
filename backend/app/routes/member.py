from flask import Blueprint, render_template, jsonify, url_for, redirect
from flask_security import current_user, login_required
from ..models import Book, db, BookLoan, user_datastore
from datetime import datetime, timedelta
from ..forms import RoleSelectForm
from .crud_api_calls import api_call

member_bp = Blueprint("member_bp", __name__)


def calculate_fine(days_late):
    fine_per_day = 1.00  # Assuming a fine of $1 per day
    return days_late * fine_per_day


def get_member_id_from_session():
    if not current_user.is_authenticated:
        raise Exception("No member logged in")
    return current_user.id

@member_bp.route("/member/home")
@login_required 
def home():
    books = Book.query.all()
    return render_template("member/home.html", books=books)


@member_bp.route('/select_role', methods=['GET', 'POST'])
@login_required  # Ensure only authenticated users can access this route
def select_role():
    form = RoleSelectForm()
    if form.validate_on_submit():
        selected_role = form.roles.data
        if selected_role.name == 'Librarian':
            return redirect(url_for('librarian_bp.home'))
        elif selected_role.name == 'Member':
            return redirect(url_for('member_bp.home'))
    return render_template('member/select_role.html', form=form)


def request_book(book_id, member_id):
    return api_call(f'books/request/{book_id}/{member_id}', method='post')

def view_loans(member_id):
    return api_call(f'loans/{member_id}', method='get')

def return_book(loan_id):
    return api_call(f'loans/return/{loan_id}', method='put')

