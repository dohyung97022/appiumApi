from sqlalchemy import Column, String
from src.sql_alchemy.domain.sql_alchemy import Base


class Agent(Base):
    __tablename__ = 'agent'
    agent_email = Column(String(50), primary_key=True, comment='요원 이메일')
    agent_password = Column(String(50), comment='요원 비밀번호')

    is_job_finished: bool = False
