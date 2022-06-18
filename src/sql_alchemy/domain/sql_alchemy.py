from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.dot_env.domain.database import Database

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
def db_setup():
    import src.automation.domain.action
    import src.automation.domain.action_action_association
    import src.automation.domain.user
    import src.automation.domain.user_action
    import src.automation.domain.user_action_log
    import src.automation.domain.macro
    Base.metadata.create_all(engine)
