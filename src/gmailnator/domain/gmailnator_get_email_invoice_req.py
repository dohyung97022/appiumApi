# 이메일 수신 내역 요청
class GmailnatorGetEmailInvoiceReq:
    # 최대 20
    limit: int = 20
    email: str

    def __init__(self, email: str):
        self.email = email

    def to_json(self):
        return {
            "limit": self.limit,
            "email": self.email
        }
