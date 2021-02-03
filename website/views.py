from flask import Blueprint ,render_template

# This file is the blueprint for the website
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


