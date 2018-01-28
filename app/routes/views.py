from app import app
from flask import render_template, session, redirect, request


@app.route('/')
def index():
    return render_template('index.html')
