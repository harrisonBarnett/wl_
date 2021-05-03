from flask import Blueprint, render_template, redirect, request, flash, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# blueprints allow us to use views accross the application
auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # searching the db for a user w/ the passed email
        user = User.query.filter_by(email=email).first()
        if user:
            # compare the db user password with password pass into login form
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                # logs the user into the current session
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route("/sign-up", methods=["POST", "GET"])
def signup():
    if request.method=="POST":
        # get data from forms by name
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        
        # check to see if email is in use
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This account already exists.', category='error')
            return redirect("/login")

        # checking for valid info
        if len(email) < 4:
            flash('Email must be at least 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be at least 2 characters', category='error')
        elif password != confirmation:
            flash('Passwords do not match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to the database
            new_user = User(
                            email=email, 
                            first_name=firstName, 
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)

# makes certain views only available when a user is logged in
@auth.route("/logout")
@login_required
def logout():
    # removes the current user from the session
    logout_user()
    return redirect(url_for('auth.login'))





### NEW VIEWS FOR NEW UI LAYOUT ###
### IS BETTER -- MUUUCH BETTER ###

@auth.route("/sign-in")
def sign_in():
    return render_template("sign-in.html")

@auth.route("/set-up")
def set_up():
    return render_template("set-up.html")