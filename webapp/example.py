import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from webapp.database import db_session
from .database import User

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/example", methods=["GET", "POST"])
def example():
    """Log user in"""
    print(User.query.all())
    
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # Ensure username was submitted
        if not request.form.get("username"):
            return
            # return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return
            # return apology("must provide password", 403)

        # Query database for username
        rows = User.query.filter_by(username=request.form.get("username")).all()
        print (rows)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0].password, request.form.get("password")):
            return
            # return apology("invalid username and/or password", 403)
        
        # Remember which user has logged in
        session["user_id"] = rows[0].id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@bp.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@bp.route("/example2", methods=["GET", "POST"])
def register():
    """Registers a new user"""
    session.clear()
    if request.method == "POST":
        # Create variables to get the data from the registration form
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # Ensure that the password is the same as the confirmation
        if password == confirmation:
            
            # Generate a hash to store into the database
            hash = generate_password_hash(password)
            
            # Create a newUser variable that stores the user object
            newUser = User(first_name=firstname, last_name=lastname, email=email, username=username, password=hash)
            
            # Add the newUser object to the database
            db_session.add(newUser)
           
            # Update the database
            db_session.commit()
        return redirect("/login")

    else:
        return render_template("register.html")