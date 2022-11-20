import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group2', __name__, url_prefix='/')

@bp.route("/rank-preferences", methods=["GET", "POST"])
def rank_preferences():
    """Rank importance of preferences"""
    return render_template("rank_preferences.html")

@bp.route("/grade_selection", methods=["GET", "POST"])
def grade_selection():
    """Select grade level of matches"""
    return render_template("grade_selection.html")

@bp.route("/group_size", methods=["GET", "POST"])
def group_size():
    """Select group size"""
    return render_template("group_size.html")

@bp.route("/location_type", methods=["GET", "POST"])
def group_location():
    """Select location type"""
    return render_template("group_location.html")

@bp.route("/location", methods=["GET", "POST"])
def location():
    """Select location"""
    return render_template("location.html")

@bp.route("/session_length", methods=["GET", "POST"])
def session_length():
    """Select session length"""
    return render_template("session_length.html")

@bp.route("/work_habits", methods=["GET", "POST"])
def work_habits():
    """Select work habits"""
    return render_template("work_habits.html")

@bp.route("/availability", methods=["GET", "POST"])
def availability():
    """Select availability (day and time)"""
    return render_template("availability.html")

@bp.route("/choose-classes", methods=["GET", "POST"])
def choose_classes():
    """Select classes in search of"""
    return render_template("choose_classes.html")