from src.automation.action.service import action_macro_service
from src.flask_socket_io.domain.flask_socket_io import app
from flask import request
from src.flask_socket_io.domain.response_entity import ResponseEntity


@app.route("/api/automation/action/macro", methods=['POST'])
def post_action_macro_relation():
    return ResponseEntity.build(
        data=action_macro_service.update_action_macro_relation(request.get_json()))


@app.route("/api/automation/action/macro/run", methods=['POST'])
def run_action_macro():
    return ResponseEntity.build(
        data=action_macro_service.run_action_macro(request.get_json()))
