from src.automation.domain.action import Action
from src.automation.domain.macro import Macro
from src.sql_alchemy.domain.sql_alchemy import session


# 행동 매크로 관계 업데이트
def update_action_macro_relation(req_action_json):

    # 호출
    action = session.query(Action) \
        .filter(Action.action_seq == req_action_json['action_seq']) \
        .first()

    # 변환
    apply_action_macro_json(action, req_action_json)

    # 커밋
    session.commit()


def apply_action_macro_json(action: Action, action_json: dict):
    for macro_json in action_json['macros']:

        # 신규
        if macro_json['macro_seq'] is None:
            macro = Macro()

        # 존재
        else:
            macro = action.get_macro(macro_json['macro_seq'])

        # 추가
        macro.apply_json(macro_json)
        action.macros.append(macro)

    # 삭제
    req_macro_seqs = action.get_macro_seqs_from_action_json(action_json)
    for macro in action.get_macros_not_in(req_macro_seqs):
        action.macros.remove(macro)
