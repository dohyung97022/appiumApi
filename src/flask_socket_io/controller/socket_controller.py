from src.flask_socket_io.domain.flask_socket_io import socketio
from flask_socketio import join_room, leave_room


@socketio.on('join_room')
def join_room_(req):
    join_room(room=req)
    print('room joined')


@socketio.on('leave_room')
def leave_room_(req):
    leave_room(room=req)
    print('room left')
