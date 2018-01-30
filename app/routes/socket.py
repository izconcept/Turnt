from time import sleep
from app import socketio, drinks
from flask_socketio import emit
from app.services.interface import *
from flask import session


@socketio.on('get turnt')
def get_turnt(payload):
    if 'drinks' in session:
        session['drinks'].append(drinks[payload['data']]['percentage'])
    else:
        session['drinks'] = [drinks[payload['data']]['percentage']]
    drink = payload['data']
    print("Your drink is being made !" + str(drink))
    bartender(drinks[drink]['portions'])


def bartender(recipe):
    print("Making your drink!" + str(recipe))
    total = sum(recipe)
    complete = 0
    give_me_some_white_bottle(recipe[1])
    complete += recipe[1]
    emit('update', {'message': 'Adding ' + str(recipe[1]) + ' ounce(s) of magic', 'percentage': complete/total})
    give_me_some_rear_bottle(recipe[0])
    complete += recipe[0]
    emit('update', {'message': 'Adding ' + str(recipe[0]) + ' ounce(s) of that good stuff', 'percentage': complete/total})
    give_me_some_green_bottle(recipe[2])
    complete += recipe[2]
    emit('update', {'message': 'Adding ' + str(recipe[0]) + ' ounce(s) of mulaa', 'percentage': complete/total})
    emit('complete')

