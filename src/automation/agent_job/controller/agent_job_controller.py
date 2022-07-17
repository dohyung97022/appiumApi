from src.automation.agent_job.model.assign_job_to_agent_req import AssignJobToAgentReq
from src.automation.agent_job.service import agent_job_service
from src.flask_socket_io.domain.flask_socket_io import app
from flask import request
from src.flask_socket_io.domain.response_entity import ResponseEntity


@app.route("/api/automation/agentJob/udid", methods=['GET'])
def assign_job_to_agent():
    return ResponseEntity.build(
        data=agent_job_service.assign_job_to_agent(AssignJobToAgentReq(request.args)))
