from sqlalchemy import Column, Integer, String
from sql_alchemy.domain.sql_alchemy import Base


# 자동화 할 계정
class User(Base):
    __tablename__ = 'user'
    user_seq = Column(Integer, primary_key=True, comment='회원 일렬번호')
    user_id = Column(String(30), comment='회원 계정')
    user_pw = Column(String(50), comment='회원 비밀번호')
    site = Column(String(100), comment='회원 자동화 사이트')

    def __init__(self, user_id: str, user_pw: str, site: str):
        self.user_id = user_id
        self.user_pw = user_pw
        self.site = site
