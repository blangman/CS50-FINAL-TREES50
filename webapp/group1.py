import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group1', __name__, url_prefix='/')

@bp.route("signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html")

@bp.route("profile", methods=["GET", "POST"])
def your_groups():
    return render_template("profile.html")

@bp.route("login", methods=["GET", "POST"])
def your_groups():
    return render_template("login.html")

@bp.route("terms-of-service", methods=["GET", "POST"])
def terms_of_service():
    return render_template("terms-of-service.html")

@bp.route("your-groups", methods=["GET", "POST"])
def your_groups():
    return render_template("your-groups.html")