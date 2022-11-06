import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group3', __name__, url_prefix='/')

@bp.route("group_profile", methods=["GET", "POST"])
def sample():
    """render_pages"""
    # Change what template is being rendered
    return render_template("group_profile.html")

@bp.route("success", methods=["GET", "POST"])
def success():
    """render_pages"""
    # Change what template is being rendered
    return render_template("success.html")

@bp.route("user_profile", methods=["GET", "POST"])
def user_profile():
    """render_pages"""
    # Change what template is being rendered
    return render_template("user_profile.html")

@bp.route("group_matches", methods=["GET", "POST"])
def group_matches():
    """render_pages"""
    # Change what template is being rendered
    return render_template("group_matches.html")

@bp.route("contact", methods=["GET", "POST"])
def contact():
    """render_pages"""
    # Change what template is being rendered
    return render_template("contact.html")

@bp.route("index", methods=["GET", "POST"])
def index():
    """render_pages"""
    # Change what template is being rendered
    return render_template("index.html")

