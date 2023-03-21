from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/") #whenever "/" is clicked, function will exceute
def home():
    return "<h1>Test</h1>" #Create HTML Header