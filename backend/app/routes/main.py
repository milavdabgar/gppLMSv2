from flask import Blueprint, render_template, url_for, redirect
from flask_security import auth_required
from ..forms import RoleSelectForm

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/select_role", methods=["GET", "POST"])
@auth_required("token", "session")
def select_role():
    form = RoleSelectForm()
    if form.validate_on_submit():
        selected_role = form.roles.data
        print(selected_role)
        if selected_role.name == "Librarian":
            return redirect(url_for("librarian_bp.home"))
        elif selected_role.name == "Member":
            return redirect(url_for("member_bp.home"))
    
    return render_template("main/select_role.html", form=form)