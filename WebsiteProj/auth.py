from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html", boolean  = True) #create HTML Paragraph for login spot

@auth.route("/logout")
def logout():
    return "<p>Logout</p>" #create HTML Paragraph for logout spot

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html") #Create HTML Paragraph for Sign Up Spot
