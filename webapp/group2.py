import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group2', __name__, url_prefix='/')

@bp.route("/sample-endpoint2", methods=["GET", "POST"])
def sample():
    """i am a sample plz change me"""
    # Change what template is being rendered
    return render_template("register.html")


@bp.route("/rank-preferences", methods=["GET", "POST"])
def rank_preferences():
    """i am a sample plz change me"""
    return render_template("rank_preferences.html")

@bp.route("/availability", methods=["GET", "POST"])
def availability():
    """i am a sample plz change me"""
    return render_template("availability.html")

@bp.route("/choose-classes", methods=["GET", "POST"])
def choose_classes():
    """i am a sample plz change me"""
    return render_template("choose_classes.html")