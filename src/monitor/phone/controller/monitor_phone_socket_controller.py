from src.flask_socket_io.domain.flask_socket_io import socketio
from src.monitor.phone.service import monitor_phone_service


@socketio.on('phone_touch')
def phone_touch(req):
    monitor_phone_service.phone_touch(req)
