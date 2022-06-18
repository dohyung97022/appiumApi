from sqlalchemy import Column, Integer, ForeignKey, Table
from src.sql_alchemy.domain.sql_alchemy import Base


# 행동 재귀적 다대다 연결
action_action_association = Table(
    'action_action_association',
    Base.metadata,
    Column('action_action_association_seq', Integer, primary_key=True, comment='행동 관계 테이블 일렬번호'),
    Column('parent_action_seq', Integer, ForeignKey('action.action_seq'), comment='부모 행동 일렬번호'),
    Column('child_action_seq', Integer, ForeignKey('action.action_seq'), comment='자식 행동 일렬번호'),
    Column('association_order', Integer, comment='관계 동작 순서')
)
