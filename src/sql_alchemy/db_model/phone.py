from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.sql_alchemy.domain.sql_alchemy import Base
from sqlalchemy_serializer import SerializerMixin


class Phone(Base, SerializerMixin):
    __tablename__ = 'phone'
    udid: str = Column(String(30), primary_key=True, comment='핸드폰 udid')
    model: str = Column(String(20), comment='모델명')

    accounts = relationship("Account", back_populates="action", foreign_keys='Account.udid')
