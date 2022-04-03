from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask (__name__)
app.config ["SECRET_KEY"] = "qwerty"
socketio = SocketIO(app)

@app.route ("/")
def start_page ():
    return render_template ("index.html")

