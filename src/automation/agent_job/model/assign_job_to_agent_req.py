class AssignJobToAgentReq:
    job: str
    agent_email: bool

    def __init__(self, request_args: dict):
        self.job = request_args['job']
        self.agent_email = request_args['agent_email']
