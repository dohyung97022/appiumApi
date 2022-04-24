from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from sql_alchemy.domain.sql_alchemy import Base
from user_action.domain.common.epoch import epoch_datetime
from datetime import timedelta, datetime


# 자동화 계정의 행동 양식
class UserAction(Base):
    __tablename__ = 'user_action'
    user_action_seq = Column(Integer, primary_key=True, comment='회원 행동 양식 일렬번호')
    user_seq = Column(Integer, ForeignKey('user.user_seq'), comment='user.user_seq 참조')
    user = relationship("User", back_populates="user_action")
    action = Column(String(30), comment='행동, enum Action 참조')
    cycle_time = Column(DateTime, comment='행동 순환 시간, epoch 기준')
    last_action_date = Column(DateTime, comment='마지막 행동 수행 시간')

    def __init__(self, action: str, cycle_time: timedelta):
        self.action = action
        self.cycle_time = epoch_datetime + cycle_time
        self.last_action_date = datetime.now()
