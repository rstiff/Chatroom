from app import Flask, socketio

app = Flask(__name__)

if __name__ == '__main__':
    socketio.run(app)