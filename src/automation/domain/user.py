from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.sql_alchemy.domain.sql_alchemy import Base


class User(Base):

    serialize_rules = ('-user_action.user',)

    # db 저장 내용
    __tablename__ = 'user'
    user_seq = Column(Integer, primary_key=True, comment='회원 일렬번호')
    user_email = Column(String(30), comment='회원 이메일')
    user_pw = Column(String(50), comment='회원 비밀번호')
    udid = Column(String(30), comment='핸드폰 고유번호')
    site = Column(String(100), comment='회원 자동화 사이트')

    user_action = relationship("UserAction")

    # faker 내용
    username: str
    name: str
    sex: str
    birthdate: datetime
    address: str

    def __init__(self, user_email: str, user_pw: str, udid: str, site: str, faker_profile: dict):
        self.user_email = user_email
        self.user_pw = user_pw
        self.udid = udid
        self.site = site

        # faker 에서 받은 정보를 입력
        for key in faker_profile:
            setattr(self, key, faker_profile[key])
