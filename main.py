from src import setup
from src.flask_socket_io.domain.flask_socket_io import socketio, app

if __name__ == '__main__':
    setup.configure()
    socketio.run(app, host='127.0.0.1', port=8082)
