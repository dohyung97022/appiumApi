from os import environ, getcwd
from dotenv import load_dotenv


# env 로드
load_dotenv(dotenv_path=getcwd() + '/src/dot_env/env/sb.env')


# env 에서 받아온 db 정보
class Sb:
    WEBSITE = 'WEBSITE'

    website = environ[WEBSITE]
