from src.automation.action.model.get_actions_req import GetActionsReq
from src.sql_alchemy.domain.sql_alchemy import session
from src.sql_alchemy.db_model.action import Action


# 행동 검색
def select_actions(get_actions_req: GetActionsReq) -> list[Action]:
    if get_actions_req.query == '' or None:
        return []

    if get_actions_req.is_like:
        return session.query(Action).filter(Action.name.like(get_actions_req.query + '%')).all()

    else:
        return session.query(Action).filter(Action.name == get_actions_req.query).all()


# 행동 반환
def select_action(action_seq) -> Action:
    return session.query(Action)\
                  .filter(Action.action_seq == action_seq)\
                  .one()
