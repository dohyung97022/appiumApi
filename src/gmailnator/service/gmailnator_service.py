from src.gmailnator.domain.common.gmailnator_endpoints import GmailnatorEndpoints
from src.gmailnator.domain.gmailnator_get_email_invoice_req import GmailnatorGetEmailInvoiceReq
from src.gmailnator.domain.gmailnator_get_email_invoice_res import GmailnatorGetEmailInvoiceRes
from src.gmailnator.domain.gmailnator_create_bulk_email_req import GmailnatorCreateBulkEmailReq
from src.gmailnator.domain.gmailnator_header import GmailnatorHeader
import requests

# https://rapidapi.com/johndevz/api/gmailnator/


# 이메일 생성
def create_email(req: GmailnatorCreateBulkEmailReq = GmailnatorCreateBulkEmailReq()) -> str:
    # 단일 건
    req.limit = 1

    # 요청
    response = requests.request(
        "POST",
        GmailnatorEndpoints.CREATE_BULK_EMAILS,
        json=req.to_json(),
        headers=GmailnatorHeader.header
    )

    # 반환
    return list(response.json())[0]


# 이메일 대량 생성
def create_bulk_emails(req: GmailnatorCreateBulkEmailReq = GmailnatorCreateBulkEmailReq()) -> list[str]:
    # 요청
    response = requests.request(
        "POST",
        GmailnatorEndpoints.CREATE_BULK_EMAILS,
        json=req.to_json(),
        headers=GmailnatorHeader.header
    )

    # 반환
    return list(response.json())


# 이메일 수신 내역 확인
def get_email_invoice(req: GmailnatorGetEmailInvoiceReq) -> list[GmailnatorGetEmailInvoiceRes]:
    # 요청
    response = requests.request(
        "POST",
        GmailnatorEndpoints.GET_EMAIL_INVOICE,
        json=req.to_json(),
        headers=GmailnatorHeader.header
    )

    # 형변환
    res_list = []
    for res in response.json():
        res_list.append(GmailnatorGetEmailInvoiceRes(res))

    # 반환
    return res_list
