from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.sql_alchemy.domain.sql_alchemy import Base
from src.automation.domain.common.epoch import epoch_datetime
from datetime import timedelta, datetime


# 자동화 계정의 행동 양식
class UserAction(Base):

    serialize_rules = ('-user.user_action', '-action.action_user')

    __tablename__ = 'user_action'
    user_action_seq = Column(Integer, primary_key=True, comment='회원 행동 양식 일렬번호')
    user_seq = Column(Integer, ForeignKey('user.user_seq'), comment='user.user_seq 참조')
    action_seq = Column(Integer, ForeignKey('action.action_seq'), comment='action.action_seq 참조')
    cycle_time = Column(DateTime, comment='행동 순환 시간, epoch 기준')
    last_action_date = Column(DateTime, comment='마지막 행동 수행 시간')

    user = relationship("User", back_populates="user_action")
    action = relationship("Action", back_populates="action_user")

    def __init__(self, cycle_time: timedelta):
        self.cycle_time = epoch_datetime + cycle_time
        self.last_action_date = datetime.now()
