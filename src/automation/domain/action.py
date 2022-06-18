from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.automation.domain.action_action_association import action_action_association
from src.sql_alchemy.domain.sql_alchemy import Base
from sqlalchemy_serializer import SerializerMixin


# 행동
class Action(Base, SerializerMixin):
    # db 저장 내용
    __tablename__ = 'action'
    action_seq: int = Column(Integer, primary_key=True, comment='행동 일렬번호')
    name: str = Column(String(15), comment='행동 이름')

    child_actions = relationship('Action',
                                 secondary=action_action_association,
                                 primaryjoin=action_seq == action_action_association.c.parent_action_seq,
                                 secondaryjoin=action_seq == action_action_association.c.child_action_seq,
                                 order_by="asc(action_action_association.c.association_order)"
                                 )
    action_user = relationship("UserAction")
    macros = relationship("Macro", back_populates="action", order_by="Macro.macro_order")

    def get_child_action(self, child_action_seq: int):
        return list(filter(lambda child_action: child_action.action_seq == child_action_seq, self.child_actions))[0]

    def get_child_actions_not_in(self, action_seqs: list[int]):
        return list(filter(lambda action: action.action_seq not in action_seqs, self.child_actions))

    @classmethod
    def get_child_action_seqs_from_action_json(cls, action_json):
        return list(map(lambda child_action: child_action['action_seq'], action_json['child_actions']))

    def get_macro(self, macro_seq: int):
        return list(filter(lambda macro: macro.macro_seq == macro_seq, self.macros))[0]

    def get_macros_not_in(self, macro_seqs: list[int]):
        return list(filter(lambda macro: macro.macro_seq not in macro_seqs, self.macros))

    @classmethod
    def get_macro_seqs_from_action_json(cls, action_json):
        return list(map(lambda macro: macro['macro_seq'], action_json['macros']))
