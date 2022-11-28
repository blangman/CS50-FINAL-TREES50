import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group1', __name__, url_prefix='/')

@bp.route("login", methods=["GET", "POST"])
def signup():
    '''Renders the signup page.'''
    return render_template("login.html")