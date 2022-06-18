from src.automation.domain.action import Action
from src.sql_alchemy.domain.sql_alchemy import session


# 행동 행동 관계 업데이트
def update_action_action_relation(req_action_json):

    # 호출
    action = session.query(Action) \
        .filter(Action.action_seq == req_action_json['action_seq']) \
        .first()

    # 변환
    apply_action_action_json(action, req_action_json)

    # 커밋
    session.commit()


def apply_action_action_json(action: Action, action_json: dict):
    action.name = action_json["name"]

    for child_action_json in action_json['child_actions']:

        # 신규
        if child_action_json['action_seq'] is None:
            child_action = Action()

        # 존재
        else:
            child_action = action.get_child_action(child_action_json['action_seq'])

        # 추가
        apply_action_action_json(child_action, child_action_json)
        action.child_actions.append(child_action)

    # 삭제
    req_child_action_seqs = action.get_child_action_seqs_from_action_json(action_json)
    for child_action in action.get_child_actions_not_in(req_child_action_seqs):
        action.child_actions.remove(child_action)

    return
