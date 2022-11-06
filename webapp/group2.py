import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from webapp.database import User

bp = Blueprint('group2', __name__, url_prefix='/')

@bp.route("/rank_preferences", methods=["GET", "POST"])
def rank_preferences():
    """render pages"""
    return render_template("rank_preferences.html")

@bp.route("/grade_selection", methods=["GET", "POST"])
def grade_selection():
    """choose grade of matches"""
    return render_template("grade_selection.html")

@bp.route("/group_size", methods=["GET", "POST"])
def group_size():
    """choose group size"""
    return render_template("group_size.html")

@bp.route("/location_type", methods=["GET", "POST"])
def group_location():
    """choose location type"""
    return render_template("group_location.html")

@bp.route("/location", methods=["GET", "POST"])
def location():
    """choose location"""
    return render_template("location.html")

@bp.route("/session_length", methods=["GET", "POST"])
def session_length():
    """choose session length"""
    return render_template("session_length.html")

@bp.route("/work_habits", methods=["GET", "POST"])
def work_habits():
    """choose work habits"""
    return render_template("work_habits.html")