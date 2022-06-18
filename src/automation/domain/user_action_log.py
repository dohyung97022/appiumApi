from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from src.sql_alchemy.domain.sql_alchemy import Base
from src.automation.domain.user_action import UserAction
from datetime import datetime


# 자동화 계정의 행동 로그
class UserActionLog(Base):
    __tablename__ = 'user_action_log'
    user_action_seq = Column(Integer, ForeignKey('user_action.user_action_seq'),
                             primary_key=True, comment='user_action.user_action_seq 참조')
    success_yn = Column(Boolean(), comment='행동 성공 여부')
    action_date = Column(DateTime, comment='행동 시작 시간')

    def __init__(self, user_action: UserAction, success_yn: bool):
        self.user_action_seq = user_action.user_action_seq
        self.success_yn = success_yn
        self.action_date = datetime.now()
