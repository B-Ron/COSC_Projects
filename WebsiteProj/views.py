from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/") #whenever "/" is clicked, function will exceute
def home():
    return render_template("home.html")