from app import app
from flask import render_template, session, redirect, request


drinks = {
    'rum_and_coke': {'name': 'Rum and Coke', 'portions': [0, 7, 1], 'percentage': '0.1', 'amount': 8, 'img': '/static/img/cocktail.png'},
    'coke': {'name': 'Coke', 'portions': [0, 8, 0], 'percentage': '0', 'amount': 8, 'img': '/static/img/softdrink.png'},
    'rum(shot)': {'name': 'Rum', 'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
    'gin_and_tonic': {'name': 'Gin and Tonic', 'portions': [1, 7, 0], 'percentage': '0.1', 'amount': 8, 'img': '/static/img/cocktail.png'},
    'tequila(shot)': {'name': 'Tequila', 'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
    'gin(shot)': {'name': 'Gin', 'portions': [1, 0, 0], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
}


@app.route('/')
def index():
    return render_template('index.html', drinks=drinks)
