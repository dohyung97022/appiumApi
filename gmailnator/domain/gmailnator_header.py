from dot_env.domain.rapid_api import RapidApi
from gmailnator.domain.common.gmailnator_endpoints import GmailnatorEndpoints


# rapid api 인증용 header
class GmailnatorHeader:
    header = {
        "X-RapidAPI-Host": GmailnatorEndpoints.RAPID_API_HOST,
        "X-RapidAPI-Key": RapidApi.api_key
    }
