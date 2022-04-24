# 이메일 수신 내역 응답
class GmailnatorGetEmailInvoiceRes:
    id: str
    from_: str
    subject: str
    date: int

    def __init__(self, my_dict):
        # dict 를 class 로 형변환
        for key in my_dict:
            setattr(self, key, my_dict[key])
