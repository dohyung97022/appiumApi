from os import environ, getcwd
from dotenv import load_dotenv


# env 로드
load_dotenv(dotenv_path=getcwd() + '/src/dot_env/env/aws.env')


# env 에서 받아온 db 정보
class AWS:
    ACCESS_KEY_ID = 'ACCESS_KEY_ID'
    SECRET_ACCESS_KEY = 'SECRET_ACCESS_KEY'

    access_key_id = environ[ACCESS_KEY_ID]
    secret_access_key = environ[SECRET_ACCESS_KEY]
