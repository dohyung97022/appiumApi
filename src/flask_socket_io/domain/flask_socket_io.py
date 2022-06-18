from os import getcwd

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

# flask 시작
app = Flask(
    __name__,
    static_folder='./templates/dist/static',
    template_folder='./templates/dist',
    root_path=getcwd()
)

# flask 설정 지정
app.config.from_object(__name__)

# flask cors 설정 지정
CORS(app, resources={
    r'/*':
        {
            'origins': [
                'http://localhost:8080', 'http://localhost:8082', 'http://127.0.0.1:8082'],
            'allow_headers': ['Access-Control-Allow-Origin', 'Content-Type']
        }
})

# socketio 시작
socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)
