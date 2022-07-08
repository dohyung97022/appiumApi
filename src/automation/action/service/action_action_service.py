from src.sql_alchemy.db_model.action import Action
from src.sql_alchemy.db_model.action_action_association import ActionActionAssociation
from src.sql_alchemy.domain.sql_alchemy import session


# 행동 행동 관계 업데이트
def update_action_action_relation(req_action_json: dict):
    # 요청 내의 모든 action_seq
    all_requested_action_seq = Action.get_all_action_seq_from_action_json(req_action_json)

    # 호출
    all_requested_actions = session.query(Action) \
        .filter(Action.action_seq.in_(all_requested_action_seq)).all()

    # root
    root_action = Action.get_action_of_seq_from_actions(all_requested_actions, req_action_json['action_seq'])

    # 변환
    apply_action_action_json(root_action, all_requested_actions, req_action_json)

    # 커밋
    session.commit()


def apply_action_action_json(action: Action, all_actions: list[Action], action_json: dict):
    # 행동 수정
    action.name = action_json["name"]

    # 미연결 관계 삭제
    req_child_action_seqs = action.get_child_action_seqs_from_action_json(action_json)
    for child_action_association in action.get_child_action_associations_not_in(req_child_action_seqs):
        action.child_action_associations.remove(child_action_association)
        session.delete(child_action_association)

    for child_action_association_json in action_json['child_action_associations']:
        child_action_json = child_action_association_json['child_action']

        # 전체 행동 중 존재
        child_action = Action.get_action_of_seq_from_actions(all_actions, child_action_json['action_seq'])

        # 핸동 신규
        if child_action is None:
            child_action = Action()

        # 관계 존재
        action_association = action.get_child_action_association_of_seq(child_action_json['action_seq'])

        # 관계 신규
        if action_association is None:
            # 관계 추가
            action_association = ActionActionAssociation(action, child_action)
            action.child_action_associations.append(action_association)

        # 관계 수정
        action_association.association_order = child_action_association_json['association_order']

        # 재귀
        apply_action_action_json(child_action, all_actions, child_action_json)

    return
