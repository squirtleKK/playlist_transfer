from os import access
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit
import sys

from get_all_playlists import *
app = Flask (__name__)
app.config ["SECRET_KEY"] = "qwerty"
socketio = SocketIO(app)

@app.route ("/")
def start_page ():
    return render_template ("index.html")

@app.route("/authtoken", methods=["GET"])
def get_token():
    data = request.args
    platform = Platform_factory.get_platform ()
    platform.get_access_token (data.get("code"))
    platform.get_playlists ()
    
    return redirect("/")

# req: https://oauth.vk.com/authorize?client_id=8132546&scope=audio&display=page&response_type=token&v=5.131
# https://accounts.spotify.com/authorize?client_id=39243b4ec71846159b2d26d29c84cae1&response_type=code&redirect_uri=http://127.0.0.1:3000/
# https://oauth.vk.com/authorize?client_id=8132546&display=page&redirect_uri=http://127.0.0.1:3000&scope=audio&response_type=code&v=5.131
if __name__ == "__main__":
    app.run (port=3000)