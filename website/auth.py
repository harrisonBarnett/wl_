from flask import Blueprint, render_template, redirect, request, flash, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# blueprints allow us to use views accross the application
auth = Blueprint('auth', __name__)

@auth.route("/logout")
@login_required # makes it to where a view is only available to a logged-in user
def logout():
    # removes the current user from the session
    logout_user()
    return redirect(url_for('auth.sign_in'))

@auth.route("/sign-in", methods=["POST", "GET"])
def sign_in():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # searching the db for a user w/ the passed email
        user = User.query.filter_by(email=email).first()
        if user:
            # compare the db user password with password pass into login form
            if check_password_hash(user.password, password):
                # logs the user into the current session
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password. try again.', category='error')
        else:
            flash('email does not exist.', category='error')

    return render_template("sign-in.html", user=current_user)

@auth.route("/set-up", methods=["POST", "GET"])
def set_up():
    if request.method=="POST":
        # get data from forms by name
        email = request.form.get('email')
        firstName = request.form.get('name')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        
        # check to see if email is in use
        user = User.query.filter_by(email=email).first()
        if user:
            flash('this account already exists.', category='error')
            return redirect("/set-up")

        # checking for valid info
        if len(email) < 4:
            flash('email must be at least 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('first name must be at least 2 characters', category='error')
        elif password != confirmation:
            flash('passwords do not match.', category='error')
        elif len(password) < 7:
            flash('password must be at least 7 characters.', category='error')
        else:
            # add user to the database
            new_user = User(
                            email=email, 
                            first_name=firstName, 
                            password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            flash('account created!', category='dark')
            return redirect(url_for('views.home'))
    
    return render_template("set-up.html", user=current_user)