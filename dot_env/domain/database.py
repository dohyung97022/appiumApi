from os import environ, getcwd
from dotenv import load_dotenv


# env 로드
load_dotenv(dotenv_path=getcwd() + '/dot_env/env/database.env')


# env 에서 받아온 db 정보
class Database:
    DATABASE_NAME = 'DATABASE_NAME'
    DATABASE_USERNAME = 'DATABASE_USERNAME'
    DATABASE_PASSWORD = 'DATABASE_PASSWORD'
    DATABASE_ENDPOINT = 'DATABASE_ENDPOINT'
    DATABASE_PORT = 'DATABASE_PORT'
    DATABASE_SCHEMA = 'DATABASE_SCHEMA'

    name = environ[DATABASE_NAME]
    username = environ[DATABASE_USERNAME]
    password = environ[DATABASE_PASSWORD]
    endpoint = environ[DATABASE_ENDPOINT]
    port = environ[DATABASE_PORT]
    schema = environ[DATABASE_SCHEMA]
