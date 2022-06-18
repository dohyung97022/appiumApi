from src.gmailnator.domain.gmailnator_get_email_invoice_req import GmailnatorGetEmailInvoiceReq
from src.gmailnator.domain.gmailnator_get_email_invoice_res import GmailnatorGetEmailInvoiceRes
from src.gmailnator.service.gmailnator_service import get_email_invoice


# 수신 메일 리스트에서 인스타그램 코드 반환 (실패시 None 반환)
def get_instagram_code_from_email(email: str):
    res_list = get_email_invoice(GmailnatorGetEmailInvoiceReq(email))
    return get_instagram_code_from_invoice_res_list(res_list)


# 수신 메일 리스트에서 인스타그램 코드 반환 (실패시 None 반환)
def get_instagram_code_from_invoice_res_list(res_list: list[GmailnatorGetEmailInvoiceRes]):
    for res in res_list:
        tmp_code = get_instagram_code_from_invoice_res(res)
        if tmp_code is not None:
            return tmp_code
    return None


# 수신 메일에서 인스타그램 코드 반환
def get_instagram_code_from_invoice_res(res: GmailnatorGetEmailInvoiceRes):
    if ' is your Instagram code' in res.subject:
        return res.subject.split(' is your Instagram code')[0]
    return None
