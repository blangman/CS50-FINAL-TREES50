import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from webapp.database import db_session
from webapp.database import Tree
import sqlite3

db = sqlite3.connect("tree.db", check_same_thread=False).cursor()


bp = Blueprint('group1', __name__, url_prefix='/')

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
    if request.method == "POST":
        leaftype = request.form.get("leaftype")
        barktype = request.form.get("barktype")
        fruittype = request.form.get("fruittype")

        if not leaftype or not barktype or not fruittype:
            flash("*Missing Required Fields*")

        else: 
            tree_name = db.execute("SELECT tree_name FROM Tree WHERE leaftype=:leaftype AND barktype=:barktype AND fruittype=:fruittype", {'leaftype': leaftype, 'barktype': barktype, 'fruittype': fruittype})
            tree = [tree[0] for tree in tree_name.fetchall()]
            print(tree_name)

            url = db.execute("SELECT image FROM Tree WHERE leaftype=:leaftype AND barktype=:barktype AND fruittype=:fruittype", {'leaftype': leaftype, 'barktype': barktype, 'fruittype': fruittype})
            image = [image[0] for image in url.fetchall()]
            print(image)

            html = db.execute("SELECT html FROM Tree WHERE leaftype=:leaftype AND barktype=:barktype AND fruittype=:fruittype", {'leaftype': leaftype, 'barktype': barktype, 'fruittype': fruittype})
            file = [file[0] for file in html.fetchall()]
            print(file)

            if len(tree) == 0:
                return redirect("not_found")
            else:
                return render_template("found.html", tree_name = tree, url = image, html = file)
            
            # final_result = [i[0] for i in cursor.fetchall()]

    return render_template("finder.html")

@bp.route('/found', methods=["GET", "POST"])
def found():
    if request.method == "POST":
        return render_template("/lobed")
    return render_template("found.html")

@bp.route('/not_found', methods=["GET", "POST"])
def not_found():
    return render_template("not_found.html")