from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask (__name__)
app.config ["SECRET_KEY"] = "qwerty"
socketio = SocketIO(app)

@app.route ("/")
def start_page ():
    return render_template ("index.html")

# req: https://oauth.vk.com/authorize?client_id=8132546&scope=audio&display=page&response_type=token&v=5.131


# https://oauth.vk.com/authorize?client_id=8132546&display=page&redirect_uri=http://127.0.0.1:3000&scope=audio&response_type=code&v=5.131
if __name__ == "__main__":
    app.run (port=3000)