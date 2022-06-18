import enum

from sqlalchemy import Column, Integer, Enum, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from src.sql_alchemy.domain.sql_alchemy import Base


class ElementType(enum.Enum):
    ID = "ID"
    XPATH = "XPATH"
    LINK_TEXT = "LINK_TEXT"
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT"
    NAME = "NAME"
    TAG_NAME = "TAG_NAME"
    CLASS_NAME = "CLASS_NAME"
    CSS_SELECTOR = "CSS_SELECTOR"


class MacroType(enum.Enum):
    CLICK = 'CLICK'
    DRAG = 'DRAG'
    SCROLL = 'SCROLL'
    RUN = 'RUN'


class Macro(Base, SerializerMixin):
    serialize_rules = ('-action.macros',)

    # db 저장 내용
    __tablename__ = 'macro'
    macro_seq = Column(Integer, primary_key=True, comment='매크로 일렬번호')
    action_seq = Column(Integer, ForeignKey("action.action_seq"))
    name = Column(String(30), comment='매크로 이름')
    element_type = Column(Enum(ElementType), comment='매크로 적용 element 종류')
    element = Column(String(30), comment='element 식별자')
    macro_type = Column(Enum(MacroType), comment='매크로 종류')
    macro_index = Column(Integer, comment='매크로 적용할 인덱스, -1일 경우 random')
    min_wait_sec = Column(Integer, comment='매크로 적용 최소 대기시간')
    max_wait_sec = Column(Integer, comment='매크로 적용 최대 대기시간')
    macro_order = Column(Integer, comment='매크로 동작 순서')

    action = relationship("Action", back_populates="macros")

    def apply_json(self, macro_json: dict):
        self.macro_seq = macro_json['macro_seq']
        self.action_seq = macro_json['action_seq']
        self.name = macro_json['name']
        self.element_type = macro_json['element_type']
        self.element = macro_json['element']
        self.macro_type = macro_json['macro_type']
        self.macro_index = macro_json['macro_index']
        self.min_wait_sec = macro_json['min_wait_sec']
        self.max_wait_sec = macro_json['max_wait_sec']
        self.macro_order = macro_json['macro_order']
