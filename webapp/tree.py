import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group1', __name__, url_prefix='/')

@bp.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@bp.route('/lobed', methods=["GET", "POST"])
def index():
    return render_template("lobed.html")

@bp.route('/pointed', methods=["GET", "POST"])
def index():
    return render_template("pointed.html")

@bp.route('/misc', methods=["GET", "POST"])
def index():
    return render_template("misc.html")

@bp.route('/needles', methods=["GET", "POST"])
def index():
    return render_template("needles.html")

@bp.route('/string', methods=["GET", "POST"])
def index():
    return render_template("string.html")

@bp.route('/teardrop', methods=["GET", "POST"])
def index():
    return render_template("teardrop.html")