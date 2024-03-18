from flask import Blueprint, redirect, url_for


bp = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@bp.route("/")
def index():
    return redirect(url_for('auth.login_user'))
