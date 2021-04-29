from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for
from .models import User
from flask_login import login_required, current_user
from . import db
import json
from . import routines


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
            if not new_squat:
                user.squat_max = user.squat_max
            else:
                user.squat_max = new_squat
            if not new_clean:
                user.clean_max = user.clean_max
            else:
                user.clean_max = new_clean
            if not new_snatch:
                user.snatch_max = user.snatch_max
            else:
                user.snatch_max = new_snatch
            db.session.commit()

            return redirect(url_for("views.home"))

    return render_template("options.html", user=current_user,
                            squat_max=current_user.squat_max,
                            clean_max=current_user.clean_max,
                            snatch_max=current_user.snatch_max)



@views.route("/squat", methods=["POST", "GET"])
@login_required
def squat():
    SQUAT_MAX = current_user.squat_max
    squat_id = current_user.squat_id
    if squat_id % 4 == 1:
        return render_template("squat.html", user=current_user, max=SQUAT_MAX, volume=routines.volume, warmup=routines.warmup, main=routines.wk_1)
    elif squat_id % 4 == 2:
        return render_template("squat.html", user=current_user, max=SQUAT_MAX, volume=routines.volume, warmup=routines.warmup, main=routines.wk_2)
    elif squat_id % 4 == 3:
        return render_template("squat.html", user=current_user, max=SQUAT_MAX, volume=routines.volume, warmup=routines.warmup, main=routines.wk_3)
    elif squat_id % 4 == 0:
        return render_template("squat.html", user=current_user, max=SQUAT_MAX, volume=routines.volume, warmup=routines.warmup, main=routines.wk_4)

@views.route("/clean", methods=["POST", "GET"])
@login_required
def clean():
    CLEAN_MAX = current_user.clean_max
    return render_template("clean.html", user=current_user, max=CLEAN_MAX, 
    three_position=routines.three_position, front_squat=routines.front_squat,
    push_press=routines.push_press, snatch_press=routines.snatch_press)