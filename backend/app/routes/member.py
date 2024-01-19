from flask import Blueprint, render_template, jsonify, url_for, redirect
from flask_security import current_user, login_required
from ..models import Book, db, BookLoan, user_datastore
from datetime import datetime, timedelta
from ..forms import RoleSelectForm

member_bp = Blueprint("member_bp", __name__)


def calculate_fine(days_late):
    fine_per_day = 1.00  # Assuming a fine of $1 per day
    return days_late * fine_per_day


def get_member_id_from_session():
    if not current_user.is_authenticated:
        raise Exception("No member logged in")
    return current_user.id


@member_bp.route("/api/books/<int:book_id>/request", methods=["POST"])
def request_book(book_id):
    # Assume member_id is obtained from session or token
    # member_id = get_member_id_from_session()

    # Create book loan
    loan = BookLoan.create(
        book_id=book_id,
        member_id=current_user.id,
        loan_date=datetime.utcnow(),
        due_date=datetime.utcnow() + timedelta(days=14),  # 2 weeks loan period
    )
    db.session.commit()

    # Update book status (if needed)

    return jsonify({"message": "Book loan created", "loan_id": loan.id}), 200


@member_bp.route("/api/books/<int:book_id>/return", methods=["POST"])
def return_book(book_id):
    # member_id = get_member_id_from_session()

    # Retrieve the loan
    loan = BookLoan.query.filter_by(
        book_id=book_id, member_id=current_user.id, returned_date=None
    ).first()
    if not loan:
        return jsonify({"error": "Loan record not found"}), 404

    # Calculate fine if overdue
    if datetime.utcnow() > loan.due_date:
        days_late = (datetime.utcnow() - loan.due_date).days
        fine = calculate_fine(days_late)

        # Update loan record with fine
        loan.fine = fine
        loan.status = "overdue"

    loan.returned_date = datetime.utcnow()
    db.session.commit()

    # Update book status (if needed)

    return (
        jsonify({"message": "Book returned", "fine": loan.fine if loan.fine else 0.0}),
        200,
    )

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
