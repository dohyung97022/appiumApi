import enum
from sqlalchemy import Column, Integer, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from src.sql_alchemy.domain.sql_alchemy import Base


class LoopType(enum.Enum):
    DAILY = 'DAILY'
    SINGLE_USE = 'SINGLE_USE'


class PhoneActionAssociation(Base, SerializerMixin):
    __tablename__ = 'phone_action_association'
    phone_action_association_seq: int = Column(Integer, primary_key=True, comment='핸드폰, 행동 관계 테이블 일렬번호')

    udid: str = Column(String(30), ForeignKey('phone.udid'), comment='핸드폰 udid')
    action_seq: int = Column(Integer, ForeignKey('action.action_seq'), comment='행동 일렬번호')
    loop: int = Column(Integer, comment='루프가 횟수')
    loop_type = Column(Enum(LoopType), comment='루프의 타입')

    phone = relationship('Phone', foreign_keys=udid, lazy="noload")
    action = relationship('Action', foreign_keys=action_seq)

    def __init__(self, phone, action):
        self.udid = phone.udid
        self.action_seq = action.action_seq
        self.action = action

    def apply_json(self, json: dict):
        self.udid = json['udid']
        self.action_seq = json['action_seq']
        self.loop = json['loop']
        self.loop_type = LoopType[json['loop_type']]
