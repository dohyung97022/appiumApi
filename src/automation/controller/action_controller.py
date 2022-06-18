from src.automation.service import action_service, action_action_service
from src.flask_socket_io.domain.flask_socket_io import app
from flask import request
from src.flask_socket_io.domain.response_entity import ResponseEntity


@app.route("/api/automation/actions", methods=['GET'])
def get_actions():
    return ResponseEntity.build(
        action_service.select_actions())


@app.route("/api/automation/action/<action_seq>", methods=['GET'])
def get_action(action_seq):
    return ResponseEntity.build(
        action_service.select_action(action_seq))


@app.route("/api/automation/action/action", methods=['POST'])
def post_action_action_relation():
    return ResponseEntity.build(
        action_action_service.update_action_action_relation(request.get_json()))
