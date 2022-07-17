import enum

from appium.webdriver.common.appiumby import AppiumBy
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

    def to_appium_by(self):
        if self is ElementType.ID: return AppiumBy.ID
        if self is ElementType.XPATH: return AppiumBy.XPATH
        if self is ElementType.LINK_TEXT: return AppiumBy.LINK_TEXT
        if self is ElementType.PARTIAL_LINK_TEXT: return AppiumBy.PARTIAL_LINK_TEXT
        if self is ElementType.NAME: return AppiumBy.NAME
        if self is ElementType.TAG_NAME: return AppiumBy.TAG_NAME
        if self is ElementType.CLASS_NAME: return AppiumBy.CLASS_NAME
        if self is ElementType.CSS_SELECTOR: return AppiumBy.CSS_SELECTOR


class MacroType(enum.Enum):
    CLICK = 'CLICK'
    DRAG = 'DRAG'
    SCROLL = 'SCROLL'
    RUN = 'RUN'
    TYPE = 'TYPE'


class DriverType(enum.Enum):
    APP = 'APP'
    WEB = 'WEB'


class MacroOperator(enum.Enum):
    NONE = 'NONE'
    TRY = 'TRY'
    OR = 'OR'


class Macro(Base, SerializerMixin):
    serialize_rules = ('-action.macros',)

    # db 저장 내용
    __tablename__ = 'macro'
    macro_seq = Column(Integer, primary_key=True, comment='매크로 일렬번호')
    action_seq = Column(Integer, ForeignKey("action.action_seq"))
    name = Column(String(100), comment='매크로 이름')
    driver_type = Column(Enum(DriverType), comment='매크로 적용 driver 종류')
    element_type = Column(Enum(ElementType), comment='매크로 적용 element 종류')
    element = Column(String(500), comment='element 식별자')
    variable = Column(String(500), comment='변수, TYPE: 입력값, RUN: 변수값')
    macro_type = Column(Enum(MacroType), comment='매크로 종류')
    macro_index = Column(Integer, comment='매크로 적용할 인덱스, -1일 경우 random')
    macro_operator = Column(Enum(MacroOperator), comment='매크로 실행조건')
    min_wait_sec = Column(Integer, comment='매크로 적용 최소 대기시간')
    max_wait_sec = Column(Integer, comment='매크로 적용 최대 대기시간')
    macro_order = Column(Integer, comment='매크로 동작 순서')

    action = relationship("Action", back_populates="macros")

    def apply_json(self, macro_json: dict):
        self.macro_seq = macro_json['macro_seq']
        self.action_seq = macro_json['action_seq']
        self.name = macro_json['name']
        self.driver_type = DriverType[macro_json['driver_type']]
        self.element_type = ElementType[macro_json['element_type']]
        self.element = macro_json['element']
        self.variable = macro_json['variable']
        self.macro_type = MacroType[macro_json['macro_type']]
        self.macro_index = macro_json['macro_index']
        self.macro_operator = MacroOperator[macro_json['macro_operator']]
        self.min_wait_sec = macro_json['min_wait_sec']
        self.max_wait_sec = macro_json['max_wait_sec']
        self.macro_order = macro_json['macro_order']
