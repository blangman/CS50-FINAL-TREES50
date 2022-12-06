import sqlite3

# Import functions that we will use from flask in the webapp. 
from flask import (
    Blueprint, flash, redirect, render_template, request
)

# connect the database that was made in database.py to tree.py so it can be accessed.
db = sqlite3.connect("tree.db", check_same_thread=False).cursor()

# Be able to create routes with bp.
bp = Blueprint('group1', __name__, url_prefix='/')

# Go through and make routes for each page of the html and render the html template for those pages.
@bp.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@bp.route('/lobed', methods=["GET", "POST"])
def lobed():
    return render_template("lobed.html")

@bp.route('/pointed', methods=["GET", "POST"])
def pointed():
    return render_template("pointed.html")

@bp.route('/misc', methods=["GET", "POST"])
def misc():
    return render_template("misc.html")

@bp.route('/needles', methods=["GET", "POST"])
def needles():
    return render_template("needles.html")

@bp.route('/string', methods=["GET", "POST"])
def string():
    return render_template("string.html")

@bp.route('/teardrop', methods=["GET", "POST"])
def teardrop():
    return render_template("teardrop.html")

@bp.route('/finder', methods=["GET", "POST"])
def finder():
    # When the submit button is clicked,
    if request.method == "POST":
        # access the information that the user submitted through the form
        leaftype = request.form.get("leaftype")
        barktype = request.form.get("barktype")
        fruittype = request.form.get("fruittype")

        # If they failed to submit something, flash method at top of screen
        if not leaftype or not barktype or not fruittype:
            flash("*Missing Required Fields*")

        # If they did submit something for each category, access the database to get the tree. 
        else: 
            # Get trees from the database where all the criteria are true
            tree_name = db.execute("SELECT tree_name FROM Tree WHERE leaftype=:leaftype AND barktype=:barktype AND fruittype=:fruittype", {'leaftype': leaftype, 'barktype': barktype, 'fruittype': fruittype})
            # turn that into a list to make it easier to manipulate and sort through. 
            tree = [tree[0] for tree in tree_name.fetchall()]
            
            # access all of the images that match the search criteria and once again put them as lists. 
            url = db.execute("SELECT image FROM Tree WHERE leaftype=:leaftype AND barktype=:barktype AND fruittype=:fruittype", {'leaftype': leaftype, 'barktype': barktype, 'fruittype': fruittype})
            image = [image[0] for image in url.fetchall()]
            
            # The same as the above db.executes but with the html for the trees that match the criteria. 
            html = db.execute("SELECT html FROM Tree WHERE leaftype=:leaftype AND barktype=:barktype AND fruittype=:fruittype", {'leaftype': leaftype, 'barktype': barktype, 'fruittype': fruittype})
            file = [file[0] for file in html.fetchall()]
            
            # if there are no trees that match the criteria, return not_found
            if len(tree) == 0:
                return redirect("not_found")
            # if trees do match the criteria, pass their information on to found.html 
            else:
                return render_template("found.html", tree_name = tree, url = image, html = file)
    
    # for when the method is get instead of post 
    return render_template("finder.html")

@bp.route('/found', methods=["GET", "POST"])
def found():
    return render_template("found.html")

@bp.route('/not_found', methods=["GET", "POST"])
def not_found():
    return render_template("not_found.html")