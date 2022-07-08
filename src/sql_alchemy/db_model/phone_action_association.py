from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from src.sql_alchemy.domain.sql_alchemy import Base


class PhoneActionAssociation(Base, SerializerMixin):
    __tablename__ = 'phone_action_association'
    phone_action_association_seq: int = Column(Integer, primary_key=True, comment='핸드폰, 행동 관계 테이블 일렬번호')

    udid: str = Column(String(30), ForeignKey('phone.udid'), comment='핸드폰 udid')
    action_seq: int = Column(Integer, ForeignKey('action.action_seq'), comment='행동 일렬번호')

    # action = relationship('Action', foreign_keys=action_seq)
    # phone = relationship('Phone', foreign_keys='Phone.udid')
