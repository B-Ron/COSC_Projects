from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    
    return render_template("login.html", boolean  = True) #create HTML Paragraph for login spot

@auth.route("/logout")
def logout():
    return "<p>Logout</p>" #create HTML Paragraph for logout spot

@auth.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
    if len(email) < 4:
        flash("Email must be longer than 3 characters", category = "error")
    elif len(firstName) <2:
        flash("First Name must be longer than 2 characters", category = "error")
    elif password1 != password2:
        flash("Passwords do not match", category = "error")
    elif len(password1) < 7:
        flash("Password shorter than 7 characters", category = "error")
    else:
        flash("Account Created!", category = "success")
        #add user to database
    return render_template("sign_up.html") #Create HTML Paragraph for Sign Up Spot
