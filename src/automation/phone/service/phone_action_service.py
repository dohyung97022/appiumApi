from src.automation.phone.model.GetPhoneActionsReq import GetPhoneActionsReq
from src.sql_alchemy.db_model.action import Action
from src.sql_alchemy.db_model.phone import Phone
from src.sql_alchemy.db_model.phone_action_association import PhoneActionAssociation
from src.sql_alchemy.domain.sql_alchemy import session


# 핸드폰 행동 리스트 조회
def select_phone_actions(args: GetPhoneActionsReq):
    # 핸드폰 조회
    return session.query(Phone) \
        .filter(Phone.udid == args.udid) \
        .first()


# 핸드폰 행동 리스트 저장
def update_phone_actions(req_json: dict):

    # 핸드폰 조회
    phone = session.query(Phone) \
        .filter(Phone.udid == req_json['udid']) \
        .first()

    # 요청 받은 관계
    action_association_seqs = phone.get_action_association_seqs_of_json(req_json['phoneActionAssociation'])

    # 조회되었지만 요청에 없는 관계
    del_action_associations = phone.get_action_associations_not_in_seqs(action_association_seqs)

    # 삭제
    for del_action_association in del_action_associations:
        phone.action_associations.remove(del_action_association)
        session.delete(del_action_association)

    # 요청의 모든 action
    for phone_action_association_json in req_json['phoneActionAssociation']:

        # 조회 내 확인
        phone_action_association = phone.get_action_association_of_seq(phone_action_association_json['phone_action_association_seq'])

        # 없다면 생성
        if phone_action_association is None:
            phone_action_association = PhoneActionAssociation(phone, Action())
            phone.action_associations.append(phone_action_association)

        # 수정
        phone_action_association.apply_json(phone_action_association_json)
        phone_action_association.action.apply_json(phone_action_association_json['action'])

    # 커밋
    session.commit()
