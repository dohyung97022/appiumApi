from src.sql_alchemy.domain.sql_alchemy import session
from src.automation.domain.action import Action


# 행동 검색
def select_actions() -> list[Action]:
    return session.query(Action).all()


# 행동 반환
def select_action(action_seq) -> Action:
    return session.query(Action).filter(Action.action_seq == action_seq).one()
