from flask import Flask, session
from flask_socketio import SocketIO, emit
from app.models.forms import UserForm

app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = 'ASDA*1esada`~9d(*$*^#dsada'

drinks = {
    'rum_and_coke': {'name': 'Rum and Coke', 'portions': [0, 4, 1], 'percentage': '0.1', 'amount': 5, 'img': '/static/img/cocktail.png'},
    'coke': {'name': 'Coke', 'portions': [0, 5, 0], 'percentage': '0', 'amount': 5, 'img': '/static/img/softdrink.png'},
    'rum(shot)': {'name': 'Rum', 'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
    'gin_and_tonic': {'name': 'Gin and Tonic', 'portions': [1, 4, 1], 'percentage': '0.1', 'amount': 6, 'img': '/static/img/cocktail.png'},
    'tequila(shot)': {'name': 'Tequila', 'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
    'martini': {'name': 'Vodka Martini', 'portions': [1, 2, 1], 'percentage': '0.3', 'amount': 4, 'img': '/static/img/martini.png'},
    'gin(shot)': {'name': 'Gin', 'portions': [1, 0, 0], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
}

from app.routes import views, socket