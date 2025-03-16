import webbrowser


from threading import Timer
from website import create_app
from flask import Flask
from flask_socketio import SocketIO

app = create_app()

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True, use_reloader=False)







