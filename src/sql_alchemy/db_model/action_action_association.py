from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from src.sql_alchemy.domain.sql_alchemy import Base


class ActionActionAssociation(Base, SerializerMixin):
    __tablename__ = 'action_action_association'
    action_action_association_seq: int = Column(Integer, primary_key=True, comment='행동 관계 테이블 일렬번호')
    association_order: int = Column(Integer, comment='관계 동작 순서')

    child_action_seq: int = Column(Integer, ForeignKey('action.action_seq'), comment='자식 행동 일렬번호')
    parent_action_seq: int = Column(Integer, ForeignKey('action.action_seq'), comment='부모 행동 일렬번호')

    child_action = relationship('Action', foreign_keys=child_action_seq)
    parent_action = relationship('Action', foreign_keys=parent_action_seq, lazy="noload")

    def __init__(self, parent_action, child_action):
        self.child_action_seq = child_action.action_seq
        self.parent_action_seq = parent_action.action_seq
        self.child_action = child_action
