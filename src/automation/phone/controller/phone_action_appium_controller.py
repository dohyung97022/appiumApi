from flask import request

from src.automation.phone.model.get_action_run_req import GetActionRunReq
from src.automation.phone.service import phone_action_appium_service
from src.flask_socket_io.domain.flask_socket_io import app
from src.flask_socket_io.domain.response_entity import ResponseEntity


@app.route("/api/automation/phone/action/appium/run", methods=['GET'])
def get_phone_action_appium_run():
    return ResponseEntity.build(
        data=phone_action_appium_service.phone_action_appium_run(GetActionRunReq(request.args)))