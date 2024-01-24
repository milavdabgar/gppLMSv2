from flask import Blueprint, jsonify, request, url_for
from flask_security import auth_required
from datetime import datetime
from ..models import db, BookLoan
from ..schemas import book_loan_schema, book_loans_schema

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/api/select_role", methods=["GET", "POST"])
@auth_required("token", "session")
def select_role():
    data = request.json
    selected_role = data.get("role")
    if selected_role:
        if selected_role == "Librarian":
            return jsonify({"redirect_url": url_for("librarian_bp.home")})
        elif selected_role == "Member":
            return jsonify({"redirect_url": url_for("member_bp.home")})
    
    return jsonify({"error": "Invalid role selected"}), 400


# Get loans for a member
@api_bp.route("/api/bookloans/members/<int:member_id>", methods=['GET'])
def get_loans_by_member(member_id):
    loans = BookLoan.query.filter_by(member_id=member_id).all()
    return book_loans_schema.jsonify(loans)



# Get loans for a book
@api_bp.route("/api/bookloans/books/<int:book_id>", methods=['GET'])
def get_loans_by_book(book_id):
    loans = BookLoan.query.filter_by(book_id=book_id).all()
    return book_loans_schema.jsonify(loans)


# Approve loan
@api_bp.route("/api/bookloans/<int:loan_id>/approve", methods=["PUT"])
def approve_loan(loan_id):
    loan = BookLoan.query.get(loan_id)
    loan.status = "approved"
    db.session.commit()
    return book_loan_schema.jsonify(loan)


# Return loan
@api_bp.route("/api/bookloans/<int:loan_id>/return", methods=["PUT"])
def return_loan(loan_id):
    loan = BookLoan.query.get(loan_id)
    loan.returned_date = datetime.utcnow().date()
    loan.status = "returned"
    db.session.commit()
    return book_loan_schema.jsonify(loan)