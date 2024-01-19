from flask import Blueprint
from datetime import datetime
from flask_restful import Resource, Api
from ..models import db, Book, BookLoan
from ..schemas import BookLoanSchema

member_api_bp = Blueprint("member_api_bp", __name__)
api = Api(member_api_bp)

class BookRequestApi(Resource):
    def post(self, book_id, member_id):
        new_loan = BookLoan(member_id=member_id, book_id=book_id, status = 'requested')
        db.session.add(new_loan)
        db.session.commit()
        return {'message': 'Book requested successfully'}, 201
api.add_resource(BookRequestApi, '/books/request/<int:book_id>/<int:member_id>')

class BookLoanApi(Resource):
    def get(self, member_id):
        loans = BookLoan.query.filter_by(member_id=member_id).all()
        return BookLoanSchema(many=True).dump(loans)
api.add_resource(BookLoanApi, '/loans/<int:member_id>')


def calculate_fine(days_late):
    fine_per_day = 1.00  # Assuming a fine of $1 per day
    return days_late * fine_per_day

class BookReturnApi(Resource):
    def put(self, loan_id):
        loan = BookLoan.query.get_or_404(loan_id)
        loan.return_date = datetime.utcnow()
        if loan.return_date > loan.due_date:
            days_late = (loan.return_date - loan.due_date).days
            fine = calculate_fine(days_late)
            loan.fine = fine
            loan.status = "overdue"
        loan.status = 'returned'
        db.session.commit()
        return {'message': 'Book returned successfully'}, 200
api.add_resource(BookReturnApi, '/loans/return/<int:loan_id>')

