from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for
from .models import User
from flask_login import login_required, current_user
from . import db
import json


# blueprints allow us to use views accross the application
views = Blueprint('views', __name__)


@views.route("/", methods=["POST", "GET"])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route("/options", methods=["POST", "GET"])
@login_required
def options():
    if request.method=="POST":
        if "update_totals" in request.form:
            new_squat = request.form.get("squat")
            new_clean = request.form.get("clean")
            new_snatch = request.form.get("snatch")

            user = User.query.get(current_user.id)

            user.squat_max = new_squat
            user.clean_max = new_clean
            user.snatch_max = new_snatch
            db.session.commit()

            return redirect(url_for("views.home"))

    return render_template("options.html", user=current_user,
                            squat_max=current_user.squat_max,
                            clean_max=current_user.clean_max,
                            snatch_max=current_user.snatch_max)