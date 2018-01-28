from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('connect')
def connect():
    print('Connect')

from app.routes import views
