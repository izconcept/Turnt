from app import app, drinks
from flask import render_template, session, redirect, request
from app.services.BAC import calculate_bac
from app.models.forms import UserForm


@app.route('/')
def index():
    return render_template('index.html', drinks=drinks)


@app.route('/tracker')
def tracker():
    return render_template('bactracker.html', )
