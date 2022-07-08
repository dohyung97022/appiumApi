class GetActionsReq:
    query: str
    is_like: bool

    def __init__(self, request_args: dict):
        self.query = request_args['query']
        self.is_like = request_args['is_like'] == 'true'
