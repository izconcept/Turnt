from flask import Flask

app = Flask(__name__)
app.secret_key = '09sda09d90suDUSADhoSHdjkha'
from app.routes import api, views