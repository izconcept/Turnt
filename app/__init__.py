from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('get turnt')
def get_turnt(payload):
    print(payload)


from app.routes import views
