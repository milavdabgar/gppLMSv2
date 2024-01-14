from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from flask import redirect, url_for, request, flash
from .extensions import db
from .models import (
    Role,
    User,
    Librarian,
    Member,
    Membership,
    Wishlist,
    Collection,
    Genre,
    Author,
    Book,
    Transaction,
    BookLoan,
    Purchase,
    Review
)


class MyModelView(ModelView):
    # def is_accessible(self):
    #     return current_user.is_active and current_user.is_authenticated and current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("security.login", next=request.url))


class UserView(MyModelView):
    def create_model(self, form):
        try:
            model = self.model()
            form.populate_obj(model)
            model.creator_id = (
                current_user.id
            )  # Set creator_id to the current user's ID
            self.session.add(model)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash("Failed to create record. " + str(ex), "error")
                # log.exception('Failed to create record.')
            self.session.rollback()

            return False
        else:
            self.after_model_change(form, model, True)

        return model


def setup_admin(app):
    # admin = Admin(app, name='GPP Admin', template_mode='bootstrap3')
    admin = Admin(
        app,
        name="GPP FlaskAdmin",
        template_mode="bootstrap3",
        url="/flask-admin",
        endpoint="flask-admin",
    )
    admin.add_view(MyModelView(Role, db.session, category="User"))
    admin.add_view(
        UserView(
            User, db.session, name="User Admin", endpoint="user_admin", category="User"
        )
    )
    admin.add_view(MyModelView(Librarian, db.session, category="User"))
    admin.add_view(MyModelView(Member, db.session, category="User"))
    admin.add_view(MyModelView(Membership, db.session, category="Account"))
    admin.add_view(MyModelView(Wishlist, db.session, category="Account"))
    admin.add_view(MyModelView(Collection, db.session, category="Account"))
    admin.add_view(MyModelView(Genre, db.session, category="BookData"))
    admin.add_view(MyModelView(Author, db.session, category="BookData"))
    admin.add_view(MyModelView(Book, db.session, category="BookData"))
    admin.add_view(MyModelView(Transaction, db.session, category="Transaction"))
    admin.add_view(MyModelView(BookLoan, db.session, category="Transaction"))
    admin.add_view(MyModelView(Purchase, db.session, category="Transaction"))
    admin.add_view(MyModelView(Review, db.session, category="BookData"))

    return admin
