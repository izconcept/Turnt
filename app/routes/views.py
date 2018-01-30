from app import app, drinks
from flask import render_template, session, redirect, request


@app.route('/')
def index():
    return render_template('index.html', drinks=drinks)
