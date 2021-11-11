import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from explorationproj.database import db_session
from explorationproj.models import User

bp = Blueprint('officers', __name__, url_prefix='/')

@bp.route("/sample-endpoint2", methods=["GET", "POST"])
def sample():
    return "not implemented"