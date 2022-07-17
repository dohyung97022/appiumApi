from flask import request

from src.automation.phone.model.get_phone_actions_req import GetPhoneActionsReq
from src.automation.phone.service import phone_action_service
from src.flask_socket_io.domain.flask_socket_io import app
from src.flask_socket_io.domain.response_entity import ResponseEntity


@app.route("/api/automation/phone/actions", methods=['POST'])
def post_phone_actions():
    return ResponseEntity.build(
        data=phone_action_service.update_phone_actions(request.get_json()))


@app.route("/api/automation/phone/actions", methods=['GET'])
def get_phone_actions():
    return ResponseEntity.build(
        data=phone_action_service.select_phone_actions(GetPhoneActionsReq(request.args)))
