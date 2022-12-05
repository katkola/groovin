from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.fuecoco import Fuecoco


@app.route('/')
def index():
    return render_template('index.html')