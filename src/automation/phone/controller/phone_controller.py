from src.automation.phone.service import phone_service
from src.config import udid_to_device
from src.flask_socket_io.domain.flask_socket_io import app
from src.flask_socket_io.domain.response_entity import ResponseEntity


@app.route("/api/automation/phones", methods=['POST'])
def post_phones():
    return ResponseEntity.build(data=phone_service.insert_phones(udid_to_device))
