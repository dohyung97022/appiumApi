class GetActionRunReq:
    action_seq: int
    udid: str

    def __init__(self, request_args: dict):
        self.action_seq = request_args['actionSeq']
        self.udid = request_args['udid']
