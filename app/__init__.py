import ast
from app.services.interface import *
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

drinks = {
    'rum_and_coke': {'name': 'Rum and Coke', 'portions': [0, 7, 1], 'percentage': '0.1', 'amount': 8, 'img': '/static/img/cocktail.png'},
    'coke': {'name': 'Coke', 'portions': [0, 8, 0], 'percentage': '0', 'amount': 8, 'img': '/static/img/softdrink.png'},
    'rum(shot)': {'name': 'Rum', 'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
    'gin_and_tonic': {'name': 'Gin and Tonic', 'portions': [1, 7, 0], 'percentage': '0.1', 'amount': 8, 'img': '/static/img/cocktail.png'},
    'tequila(shot)': {'name': 'Tequila', 'portions': [0, 0, 1], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
    'gin(shot)': {'name': 'Gin', 'portions': [1, 0, 0], 'percentage': '0.4', 'amount': 1, 'img': '/static/img/shot.png'},
}

@socketio.on('get turnt')
def get_turnt(payload):
    drink = payload['data']
    print("Your drink is being made !" + str(drink))
    bartender(drinks[drink]['portions'])

def bartender(recipe):
    print("Making your drink!" + str(recipe))
    give_me_some_white_bottle(recipe[1])
    # give_me_some_rear_bottle(recipe[0])
    # give_me_some_green_bottle(recipe[2])



from app.routes import views


