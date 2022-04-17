from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dot_env.domain.database import Database

# 연결 설정
engine = create_engine(
    f'{Database.name}'
    f'://{Database.username}'
    f':{Database.password}'
    f'@{Database.endpoint}'
    f':{Database.port}'
    f'/{Database.schema}'
    f'?charset=utf8', echo=True)

# 세션을 통해 db 와 연결
session = sessionmaker(engine)()

# db 베이스
Base = declarative_base()


# db 에 생성되지 않은 객체들이 있다면 생성
def setup():
    Base.metadata.create_all(engine)
