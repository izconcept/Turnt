from app import app
from flask import render_template, session, redirect, request


drinks = {
    'rum_and_coke': {'portions': [0, 7, 1], 'percentage': '0.1', 'amount': 8},
    'coke': {'portions': [0, 8, 0], 'percentage': '0', 'amount': 8},
    'rum(shot)': {'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1},
    'tequila(shot)': {'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1},
    'gin(shot)': {'portions': [1, 0, 0], 'percentage': '0.4', 'amount': 1},
    'gin_and_tonic': {'portions': [1, 7, 0], 'percentage': '0.1', 'amount': 8},
}


@app.route('/')
def index():
    return render_template('index.html', drinks=drinks)
