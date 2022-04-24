# 이메일 대량 생산 요청
class GmailnatorCreateBulkEmailReq:
    # 최대 500
    limit: int = 500
    public_mail: bool = True
    public_plus_gmail: bool = True
    public_dot_gmail: bool = True
    private_mail: bool = False
    private_plus_gmail: bool = False
    private_dot_gmail: bool = False

    def __init__(self) -> None:
        super().__init__()

    def get_options_as_list(self) -> list[int]:
        option_list = []
        if self.public_mail is True:
            option_list.append(1)
        if self.public_plus_gmail is True:
            option_list.append(2)
        if self.public_dot_gmail is True:
            option_list.append(3)
        if self.private_mail is True:
            option_list.append(4)
        if self.private_plus_gmail is True:
            option_list.append(5)
        if self.private_dot_gmail is True:
            option_list.append(6)
        return option_list

    def to_json(self):
        return {
            "limit": self.limit,
            "options": self.get_options_as_list()
        }
