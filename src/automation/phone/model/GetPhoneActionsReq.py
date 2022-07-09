class GetPhoneActionsReq:
    udid: str

    def __init__(self, request_args: dict):
        self.udid = request_args['udid']
