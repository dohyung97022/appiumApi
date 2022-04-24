from os import environ, getcwd
from dotenv import load_dotenv


# env 로드
load_dotenv(dotenv_path=getcwd() + '/dot_env/env/rapid_api.env')


# env 에서 받아온 db 정보
class RapidApi:
    API_KEY = 'API_KEY'

    api_key = environ[API_KEY]
